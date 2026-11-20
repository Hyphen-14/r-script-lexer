"""
=============================================================================
Compilation Technique (Class LD07) - Group Assignment Project 1
Lexical Analyzer Development using Python PLY

Group : Group 2 — R-Like Scripting
Case  : 3. Simple Conditional IF with Block (Slide 19)
PIC   : 2802431395 - Samuel Tristan Ryansyah

Members:
  1. 2802438754 - Nathasa Bintang Kayesa
  2. 2802495051 - Yasin Taryaqil Aghyar
  3. 2802521932 - Athallah Rafif Rijal Belvana
  4. 2802431395 - Samuel Tristan Ryansyah
  5. 2802515261 - Early Achiril Putra
=============================================================================

PETUNJUK PENGERJAAN (KASUS 3 — SIMPLE CONDITIONAL IF WITH BLOCK):
-----------------------------------------------------------------
Target Input Source Code (Slide 19 / sample_inputs/case3_input.R):
    #R version 3.4.4 
    num1 <- 10
    num2 <- 20
    if (num1>num2) {
    bignum <- num1;
    cat("Big Number is ", bignum, "\\n")
    } else {
    bignum <- num2;
    cat("Big Number is ", bignum, "\\n")
    }

Yang perlu diimplementasikan menggunakan `ply.lex`:
1. Definisikan `reserved` untuk keyword kondisional & output:
   - "if" -> "IF", "else" -> "ELSE", "cat" -> "CAT", "print" -> "PRINT".
2. Definisikan `tokens`:
   - ID, NUMBER, STRING, ASSIGN (`<-`)
   - Operator aritmatika: PLUS, MINUS, TIMES, DIVIDE
   - Operator relasional: LE (`<=`), GE (`>=`), EQ (`==`), NE (`!=`), LT (`<`), GT (`>`)
   - Delimiter blok & statement: LPAREN, RPAREN, LBRACE (`{`), RBRACE (`}`), COMMA, SEMICOLON (`;`)
   - Nilai dari `reserved`.
   *Tips: Pastikan operator multi-karakter (`<=`, `>=`, `==`, `!=`, `<-`) terdeteksi dengan benar.*
3. Buat aturan `t_COMMENT(t)` (`r"\\#[^\\n]*"`) agar baris komentar `#R version 3.4.4`
   diabaikan dan tidak menghasilkan error.
4. Lengkapi `t_STRING`, `t_NUMBER`, `t_ID`, `t_newline`, `t_ignore`, dan `t_error`.
5. Jalankan lexer terhadap `DEFAULT_SOURCE` dan cetak tabel token lengkap.

Referensi aturan token lengkap dapat dilihat di `src/r_lexer.py` dan `README.md`.
=============================================================================
"""


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


# ---------------------------------------------------------------------------
# 1. Reserved words (keyword & fungsi output bawaan)
#    Dicocokkan lewat t_ID: kata yang ada di dictionary ini diubah tipenya
#    dari ID menjadi token keyword.
# ---------------------------------------------------------------------------
reserved = {
    "if": "IF",
    "else": "ELSE",
    "cat": "CAT",
    "print": "PRINT",
}

# ---------------------------------------------------------------------------
# 2. Daftar token
# ---------------------------------------------------------------------------
tokens = [
    # Literal & identifier
    "ID",
    "NUMBER",
    "STRING",
    # Assignment
    "ASSIGN",
    # Operator aritmatika
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    # Operator relasional
    "LE",
    "GE",
    "EQ",
    "NE",
    "LT",
    "GT",
    # Delimiter blok & statement
    "LPAREN",
    "RPAREN",
    "LBRACE",
    "RBRACE",
    "COMMA",
    "SEMICOLON",
] + list(dict.fromkeys(reserved.values()))  # IF, ELSE, CAT, PRINT (tanpa duplikat)

# ---------------------------------------------------------------------------
# 3. Aturan token berbentuk string
#    PLY mengurutkan aturan string dari regex TERPANJANG ke terpendek, sehingga
#    operator dua karakter (<-, <=, >=, ==, !=) selalu dicoba lebih dulu
#    daripada operator satu karakter (<, >). Inilah prinsip "longest match".
# ---------------------------------------------------------------------------
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

# Karakter yang diabaikan (spasi, tab, carriage return dari file Windows)
t_ignore = " \t\r"


# ---------------------------------------------------------------------------
# 4. Aturan token berbentuk fungsi
#    Aturan fungsi dicoba sesuai URUTAN penulisan, dan SEBELUM aturan string.
#    Karena itu komentar harus ditulis paling awal supaya "3.4.4" di dalam
#    "#R version 3.4.4" tidak sempat dibaca sebagai NUMBER.
# ---------------------------------------------------------------------------
def t_COMMENT(t):
    r"\#[^\n]*"
    # Komentar R diawali '#' sampai akhir baris. Tidak mengembalikan token.
    pass


def t_STRING(t):
    r'["\u201c](?:\\.|[^"\\\u201d\n])*["\u201d]|[\'\u2018](?:\\.|[^\'\\\u2019\n])*[\'\u2019]'
    # Mendukung "..." , '...' , dan smart quote “...”.
    # "\\n" di dalam string tetap 2 karakter (backslash + n), bukan newline.
    t.value = t.value[1:-1]
    return t


def t_NUMBER(t):
    r"\d+(?:\.\d+)?"
    t.value = float(t.value) if "." in t.value else int(t.value)
    return t


def t_ID(t):
    r"[a-zA-Z_][a-zA-Z0-9_.]*"
    t.type = reserved.get(t.value, "ID")  # if/else/cat/print -> keyword
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def find_column(text, lexpos):
    """Kolom 1-based dari awal baris saat ini."""
    last_newline = text.rfind("\n", 0, lexpos)
    if last_newline < 0:
        return lexpos + 1
    return lexpos - last_newline


def t_error(t):
    col = find_column(t.lexer.lexdata, t.lexpos)
    t.lexer.errors.append((t.lexer.lineno, col, t.value[0]))
    t.lexer.skip(1)  # lewati karakter ilegal, lanjutkan pemindaian


# ---------------------------------------------------------------------------
# 5. Fungsi utama
# ---------------------------------------------------------------------------
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
