# Case 1: Simple Statement
# Group 2 - LD07

import argparse
import sys
import ply.lex as lex

DEFAULT_SOURCE = """print("Hello, world!")
cat(“Thanks")
"""

# Reserved keywords
reserved = {
    "print": "PRINT",
    "cat": "CAT",
}

# Token list
tokens = [
    "ID",
    "STRING",
    "LPAREN",
    "RPAREN",
    "COMMA",
] + list(reserved.values())

# Delimiter regex rules
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_COMMA = r","

# Ignored whitespace
t_ignore = " \t\r"


# Complex token rules
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


# Error handling
def t_error(t):
    print(f"Lexical error at line {t.lexer.lineno}: illegal character {t.value[0]!r}")
    t.lexer.skip(1)


# Build and run lexer
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