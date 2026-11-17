"""
=============================================================================
Compilation Technique (Class LD07) - Group Assignment Project 1
Master CLI Runner for Group 2 — R-Like Scripting Lexical Analyzer

PIC : 2802521932 - Athallah Rafif Rijal Belvana

Penggunaan:
    python run_all.py                                  # jalankan 4 kasus + ringkasan
    python run_all.py --file sample_inputs/case2_input.R   # satu file .R tertentu
    python run_all.py --quiet                          # hanya ringkasan
=============================================================================
"""

import argparse
import sys
from pathlib import Path

from src.r_lexer import format_token_table, tokenize_code

BASE_DIR = Path(__file__).resolve().parent

SAMPLE_CASES = [
    ("Case 1 - Simple Statement", BASE_DIR / "sample_inputs" / "case1_input.R"),
    ("Case 2 - Simple Arithmetic Expression", BASE_DIR / "sample_inputs" / "case2_input.R"),
    ("Case 3 - Conditional IF with Block", BASE_DIR / "sample_inputs" / "case3_input.R"),
    ("Case 4 - Looping with Conditional IF", BASE_DIR / "sample_inputs" / "case4_input.R"),
]


def run_case(title, path, quiet=False):
    """Jalankan lexer pada satu file; kembalikan (total token, total error)."""
    source = Path(path).read_text(encoding="utf-8")
    if not quiet:
        print(format_token_table(source, title=title))
        print()
    tokens, errors = tokenize_code(source)
    return len(tokens), len(errors)


def print_summary(rows):
    line = "=" * 74
    print(line)
    print(" SUMMARY")
    print(line)
    print(f"{'Case':<42} | {'Tokens':>6} | {'Errors':>6}")
    print("-" * 74)
    for title, n_tok, n_err in rows:
        print(f"{title:<42} | {n_tok:>6} | {n_err:>6}")
    print("-" * 74)
    print(
        f"{'TOTAL':<42} | {sum(r[1] for r in rows):>6} | {sum(r[2] for r in rows):>6}"
    )
    print(line)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="R-Like Lexer - CLI runner")
    parser.add_argument("--file", help="jalankan hanya file .R tertentu")
    parser.add_argument("--quiet", action="store_true", help="tampilkan ringkasan saja")
    args = parser.parse_args()

    if args.file:
        path = Path(args.file)
        if not path.is_file():
            parser.error(f"file tidak ditemukan: {path}")
        cases = [(path.name, path)]
    else:
        cases = SAMPLE_CASES

    rows = []
    for title, path in cases:
        n_tok, n_err = run_case(title, path, quiet=args.quiet)
        rows.append((title, n_tok, n_err))

    print_summary(rows)


if __name__ == "__main__":
    main()
