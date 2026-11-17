"""
Core Lexical Analyzer for R-Like Scripting using Python PLY (ply.lex).

Group 2 - Compilation Technique (Class LD07) - BINUS University
Members:
- 2802438754 - Nathasa Bintang Kayesa
- 2802495051 - Yasin Taryaqil Aghyar
- 2802521932 - Athallah Rafif Rijal Belvana
- 2802431395 - Samuel Tristan Ryansyah
- 2802515261 - Early Achiril Putra
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import ply.lex as lex


@dataclass(frozen=True)
class TokenRecord:
    """Represents a single lexical token emitted by the R-Like lexer."""

    line: int
    column: int
    token_type: str
    value: object
    lexpos: int


@dataclass(frozen=True)
class LexerErrorRecord:
    """Represents an unrecognized character encountered during tokenization."""

    line: int
    column: int
    character: str
    lexpos: int


reserved = {
    "print": "PRINT",
    "cat": "CAT",
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "for": "FOR",
    "in": "IN",
    "function": "FUNCTION",
    "repeat": "REPEAT",
    "break": "BREAK",
    "next": "NEXT",
    "TRUE": "BOOLEAN",
    "FALSE": "BOOLEAN",
    "NULL": "NULL",
}

tokens = [
    "ID",
    "NUMBER",
    "STRING",
    # Assignment & Arithmetic Operators
    "ASSIGN",
    "MODULO",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    # Relational Operators
    "LE",
    "GE",
    "EQ",
    "NE",
    "LT",
    "GT",
    # Delimiters & Punctuation
    "LPAREN",
    "RPAREN",
    "LBRACE",
    "RBRACE",
    "COMMA",
    "SEMICOLON",
] + sorted(set(reserved.values()))

# Multi-character operators must precede single-character rules when ambiguous,
# though PLY sorts string regexes by descending length.
t_ASSIGN = r"<-"
t_MODULO = r"%%"
t_LE = r"<="
t_GE = r">="
t_EQ = r"=="
t_NE = r"!="

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LT = r"<"
t_GT = r">"

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_COMMA = r","
t_SEMICOLON = r";"

t_ignore = " \t\r"


def t_COMMENT(t: lex.LexToken) -> None:
    r"\#[^\n]*"
    # Comments in R begin with '#' and continue until the end of the line.
    return None


def t_STRING(t: lex.LexToken) -> lex.LexToken:
    r'["\u201c](?:\\.|[^"\\\u201d\n])*["\u201d]|[\'\u2018](?:\\.|[^\'\\\u2019\n])*[\'\u2019]'
    # Supports straight quotes ("...", '...') as well as smart quotes (“...") from slides.
    t.value = t.value[1:-1]
    return t


def t_NUMBER(t: lex.LexToken) -> lex.LexToken:
    r"\d+(?:\.\d+)?"
    t.value = float(t.value) if "." in t.value else int(t.value)
    return t


def t_ID(t: lex.LexToken) -> lex.LexToken:
    r"[a-zA-Z_][a-zA-Z0-9_.]*"
    t.type = reserved.get(t.value, "ID")
    return t


def t_newline(t: lex.LexToken) -> None:
    r"\n+"
    t.lexer.lineno += len(t.value)


def find_column(source_text: str, lexpos: int) -> int:
    """Compute 1-based column offset from the start of the current line."""
    last_newline = source_text.rfind("\n", 0, lexpos)
    if last_newline < 0:
        return lexpos + 1
    return lexpos - last_newline


def t_error(t: lex.LexToken) -> None:
    col = find_column(t.lexer.lexdata, t.lexpos)
    t.lexer.errors.append(
        LexerErrorRecord(
            line=t.lexer.lineno,
            column=col,
            character=t.value[0],
            lexpos=t.lexpos,
        )
    )
    t.lexer.skip(1)


def build_lexer(**kwargs) -> lex.Lexer:
    """Create a fresh PLY lexer instance with an isolated error buffer."""
    lexer = lex.lex(**kwargs)
    lexer.errors = []
    return lexer


def tokenize_code(source_code: str) -> tuple[list[TokenRecord], list[LexerErrorRecord]]:
    """Tokenize R-like source code and return both tokens and lexical errors."""
    lexer = build_lexer()
    lexer.input(source_code)

    token_records: list[TokenRecord] = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        col = find_column(source_code, tok.lexpos)
        token_records.append(
            TokenRecord(
                line=tok.lineno,
                column=col,
                token_type=tok.type,
                value=tok.value,
                lexpos=tok.lexpos,
            )
        )

    return token_records, list(lexer.errors)


def format_token_table(
    source_code: str,
    title: str = "R-Like Lexical Analysis Output",
) -> str:
    """Return a clean tabular report of tokens and any lexical errors."""
    token_records, error_records = tokenize_code(source_code)
    counts = Counter(tok.token_type for tok in token_records)

    lines: list[str] = [
        "=" * 74,
        f" {title}",
        "=" * 74,
        f"{'No':<4} | {'Line':<4} | {'Col':<4} | {'Token Type':<14} | {'Lexeme / Value'}",
        "-" * 74,
    ]

    for idx, tok in enumerate(token_records, start=1):
        display_val = repr(tok.value)
        lines.append(
            f"{idx:<4} | {tok.line:<4} | {tok.column:<4} | {tok.token_type:<14} | {display_val}"
        )

    lines.append("-" * 74)
    lines.append(f"Total Tokens : {len(token_records)}")
    lines.append(f"Lexical Errors: {len(error_records)}")

    if error_records:
        lines.append("")
        lines.append("Detected Lexical Errors:")
        for err in error_records:
            lines.append(
                f"  - Line {err.line}, Col {err.column}: Illegal character {repr(err.character)}"
            )

    if counts:
        summary = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
        lines.append(f"Token Breakdown: {summary}")

    lines.append("=" * 74)
    return "\n".join(lines)
