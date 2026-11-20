"""
=============================================================================
Compilation Technique (Class LD07) - Group Assignment Project 1
Lexical Analyzer Development using Python PLY

Group : Group 2 — R-Like Scripting
Case  : 1. Simple Statement (Slide 17)
PIC   : 2802438754 - Nathasa Bintang Kayesa

Members:
  1. 2802438754 - Nathasa Bintang Kayesa
  2. 2802495051 - Yasin Taryaqil Aghyar
  3. 2802521932 - Athallah Rafif Rijal Belvana
  4. 2802431395 - Samuel Tristan Ryansyah
  5. 2802515261 - Early Achiril Putra
=============================================================================

PETUNJUK PENGERJAAN (KASUS 1 — SIMPLE STATEMENT):
-------------------------------------------------
Target Input Source Code (Slide 17 / sample_inputs/case1_input.R):
    print("Hello, world!")
    cat(“Thanks")

Yang perlu diimplementasikan menggunakan `ply.lex`:
1. Definisikan dictionary `reserved` untuk keyword fungsi output:
   - "print" -> "PRINT"
   - "cat"   -> "CAT"
2. Definisikan list `tokens` yang diperlukan:
   - ID, STRING, LPAREN, RPAREN, COMMA, serta nilai dari `reserved`.
3. Buat aturan regex untuk token sederhana & terabaikan:
   - `t_LPAREN`, `t_RPAREN`, `t_COMMA`, `t_ignore = " \\t\\r"`.
4. Buat fungsi token untuk:
   - `t_STRING`: mendukung tanda kutip ganda standar ("...") maupun smart quotes (“...")
     seperti pada `cat(“Thanks")` di slide soal.
   - `t_ID`: mencocokkan identifier dan memeriksa `reserved`.
   - `t_newline`: menambah `t.lexer.lineno` sesuai jumlah newline.
   - `t_error`: menampilkan pesan error leksikal dengan nomor baris dan memanggil `t.lexer.skip(1)`.
5. Bangun lexer (`lex.lex()`), jalankan terhadap `DEFAULT_SOURCE` atau file `--file`,
   dan cetak tabel output berisi: No, Line, Token Type, dan Lexeme / Value.

Referensi aturan token lengkap dapat dilihat di `src/r_lexer.py` dan `README.md`.
=============================================================================
"""

import ply.lex as lex  # noqa: F401

DEFAULT_SOURCE = """print("Hello, world!")
cat(“Thanks")
"""

# TODO (Nathasa): Lengkapi definisi `reserved`, `tokens`, aturan `t_*`,
# serta fungsi utama untuk menjalankan lexer pada `DEFAULT_SOURCE`.
import sys
import argparse

DEFAULT_SOURCE = """print("Hello, world!")
cat(“Thanks")
"""

reserved = {
    "print": "PRINT",
    "cat": "CAT",
}

tokens = [
    "ID",
    "STRING",
    "LPAREN",
    "RPAREN",
    "COMMA",
] + list(reserved.values())

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_COMMA = r","

t_ignore = " \t\r"


def t_STRING(t):
    r'["\u201c][^"\u201c\u201d\n]*["\u201d]'
    return t


def t_ID(t):
    r"[A-Za-z_][A-Za-z0-9_]*"
    t.type = reserved.get(t.value, "ID")
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Lexical error at line {t.lexer.lineno}: illegal character {t.value[0]!r}")
    t.lexer.skip(1)


lexer = lex.lex()


def run_lexer(source):
    lexer.lineno = 1
    lexer.input(source)

    print("=" * 70)
    print(f"{'No':<5}{'Line':<8}{'Token Type':<18}{'Lexeme / Value'}")
    print("-" * 70)

    count = 0

    for tok in lexer:
        count += 1
        print(f"{count:<5}{tok.lineno:<8}{tok.type:<18}{tok.value}")

    print("-" * 70)
    print(f"Total tokens: {count}")
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="Case 1 - Simple Statement Lexer (PLY)"
    )
    parser.add_argument("--file", help="Path ke file source R (opsional)")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            source = f.read()
    else:
        source = DEFAULT_SOURCE

    run_lexer(source)


if __name__ == "__main__":
    main()