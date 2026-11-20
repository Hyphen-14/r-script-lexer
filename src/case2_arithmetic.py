# Case 2: Arithmetic Expression
# Group 2 - LD07

import argparse
import sys
from collections import Counter

import ply.lex as lex

DEFAULT_SOURCE = """num1 <- 10
num2 <- 20
num3 <- 30
sum <- num1+num2+num3
avg <- sum / 3
cat("num1 is ", num1, "\\n")
cat("num2 is ", num2, "\\n")
cat("num3 is ", num3, "\\n")
cat("Sum 3 numbers is ", sum, "\\n")
cat("Average is ", avg, "\\n")
"""

# Reserved keywords
reserved = {
    "print": "PRINT",
    "cat": "CAT",
}

tokens = [
    "ID",
    "NUMBER",
    "STRING",
    "ASSIGN",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "LPAREN",
    "RPAREN",
    "COMMA",
] + list(reserved.values())

# Operator and delimiter rules
t_ASSIGN = r"<-"
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_COMMA = r","

# Ignored whitespace
t_ignore = " \t\r"


# Complex token rules
def t_STRING(t):
    r'["“](?:\\.|[^"\\”\n])*["”]'
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
def _column(data, lexpos):
    return lexpos - data.rfind("\n", 0, lexpos)


def t_error(t):
    col = _column(t.lexer.lexdata, t.lexpos)
    t.lexer.errors.append((t.lexer.lineno, col, t.value[0]))
    print(
        f"[Lexical Error] Line {t.lexer.lineno}, Col {col}: "
        f"illegal character {t.value[0]!r}",
        file=sys.stderr,
    )
    t.lexer.skip(1)


# Lexer runner and output
def run_lexer(source):
    lexer = lex.lex()
    lexer.errors = []
    lexer.lineno = 1
    lexer.input(source)
    result = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        result.append((tok, _column(source, tok.lexpos)))
    return result, lexer.errors


def print_token_table(source):
    toks, errors = run_lexer(source)
    line = "=" * 70
    print(line)
    print(" Case 2 - Simple Arithmetic Expression (Lexical Analysis)")
    print(line)
    print(f"{'No':<4} | {'Line':<4} | {'Col':<4} | {'Token Type':<12} | Lexeme / Value")
    print("-" * 70)
    for no, (tok, col) in enumerate(toks, start=1):
        print(f"{no:<4} | {tok.lineno:<4} | {col:<4} | {tok.type:<12} | {tok.value!r}")
    print("-" * 70)
    print(f"Total Tokens  : {len(toks)}")
    print(f"Lexical Errors: {len(errors)}")
    counts = Counter(t.type for t, _ in toks)
    print("Token Breakdown: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    print(line)
    return len(toks), len(errors)


def main():
    parser = argparse.ArgumentParser(description="Case 2 lexer (arithmetic)")
    parser.add_argument("--file", help="path file .R (default: DEFAULT_SOURCE)")
    args = parser.parse_args()
    if args.file:
        with open(args.file, encoding="utf-8") as f:
            source = f.read()
    else:
        source = DEFAULT_SOURCE
    print_token_table(source)


if __name__ == "__main__":
    main()
