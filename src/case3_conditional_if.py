# Case 3: Conditional IF Block
# Group 2 - LD07

import argparse
import sys
from collections import Counter

import ply.lex as lex

DEFAULT_SOURCE = """#R version 3.4.4 
num1 <- 10
num2 <- 20
if (num1>num2) {
bignum <- num1;
cat("Big Number is ", bignum, "\\n")
} else {
bignum <- num2;
cat("Big Number is ", bignum, "\\n")
}
"""

# Reserved keywords
reserved = {
    "if": "IF",
    "else": "ELSE",
    "cat": "CAT",
    "print": "PRINT",
}

# Token list
tokens = [
    "ID",
    "NUMBER",
    "STRING",
    "ASSIGN",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "LE",
    "GE",
    "EQ",
    "NE",
    "LT",
    "GT",
    "LPAREN",
    "RPAREN",
    "LBRACE",
    "RBRACE",
    "COMMA",
    "SEMICOLON",
] + list(dict.fromkeys(reserved.values()))

# Operator and delimiter rules
t_ASSIGN = r"<-"
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

# Ignored whitespace
t_ignore = " \t\r"


# Complex token rules
def t_COMMENT(t):
    r"\#[^\n]*"
    pass


def t_STRING(t):
    r'["\u201c](?:\\.|[^"\\\u201d\n])*["\u201d]|[\'\u2018](?:\\.|[^\'\\\u2019\n])*[\'\u2019]'
    t.value = t.value[1:-1]
    return t


def t_NUMBER(t):
    r"\d+(?:\.\d+)?"
    t.value = float(t.value) if "." in t.value else int(t.value)
    return t


def t_ID(t):
    r"[a-zA-Z_][a-zA-Z0-9_.]*"
    t.type = reserved.get(t.value, "ID")
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# Column and error handling
def find_column(text, lexpos):
    last_newline = text.rfind("\n", 0, lexpos)
    if last_newline < 0:
        return lexpos + 1
    return lexpos - last_newline


def t_error(t):
    col = find_column(t.lexer.lexdata, t.lexpos)
    t.lexer.errors.append((t.lexer.lineno, col, t.value[0]))
    t.lexer.skip(1)


# Lexer builder and runner
def build_lexer():
    lexer = lex.lex(module=sys.modules[__name__])
    lexer.errors = []
    lexer.lineno = 1
    return lexer


def run_lexer(source, title="Case 3 - Simple Conditional IF with Block"):
    lexer = build_lexer()
    lexer.input(source)

    rows = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        rows.append((tok.lineno, find_column(source, tok.lexpos), tok.type, tok.value))

    width = 70
    print("=" * width)
    print(f" {title}")
    print("=" * width)
    print(f"{'No':<4} | {'Line':<4} | {'Col':<4} | {'Token Type':<10} | Lexeme / Value")
    print("-" * width)
    for no, (line, col, ttype, value) in enumerate(rows, start=1):
        print(f"{no:<4} | {line:<4} | {col:<4} | {ttype:<10} | {value!r}")
    print("-" * width)
    print(f"Total Tokens  : {len(rows)}")
    print(f"Lexical Errors: {len(lexer.errors)}")
    for line, col, ch in lexer.errors:
        print(f"  - Line {line}, Col {col}: Illegal character {ch!r}")
    counts = Counter(r[2] for r in rows)
    print("Token Breakdown: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    print("=" * width)
    return rows, lexer.errors


def main():
    parser = argparse.ArgumentParser(description="Case 3 lexer (R-Like, PLY)")
    parser.add_argument("--file", help="Path ke file .R (default: DEFAULT_SOURCE)")
    args = parser.parse_args()

    if args.file:
        with open(args.file, encoding="utf-8") as fh:
            source = fh.read()
    else:
        source = DEFAULT_SOURCE
    run_lexer(source)


if __name__ == "__main__":
    main()
