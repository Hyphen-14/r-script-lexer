"""
=============================================================================
Compilation Technique (Class LD07) - Group Assignment Project 1
Lexical Analyzer Development using Python PLY

Group : Group 2 — R-Like Scripting
Case  : 2. Simple Arithmetic Expression (Slide 18)
PIC   : 2802521932 - Athallah Rafif Rijal Belvana

Members:
  1. 2802438754 - Nathasa Bintang Kayesa
  2. 2802495051 - Yasin Taryaqil Aghyar
  3. 2802521932 - Athallah Rafif Rijal Belvana
  4. 2802431395 - Samuel Tristan Ryansyah
  5. 2802515261 - Early Achiril Putra
=============================================================================

PETUNJUK PENGERJAAN (KASUS 2 — SIMPLE ARITHMETIC EXPRESSION):
-------------------------------------------------------------
Target Input Source Code (Slide 18 / sample_inputs/case2_input.R):
    num1 <- 10
    num2 <- 20
    num3 <- 30
    sum <- num1+num2+num3
    avg <- sum / 3
    cat("num1 is ", num1, "\\n")
    cat("num2 is ", num2, "\\n")
    cat("num3 is ", num3, "\\n")
    cat("Sum 3 numbers is ", sum, "\\n")
    cat("Average is ", avg, "\\n")

Yang perlu diimplementasikan menggunakan `ply.lex`:
1. Definisikan `reserved` ("print": "PRINT", "cat": "CAT").
2. Definisikan `tokens`:
   - ID, NUMBER, STRING
   - ASSIGN (`<-`)
   - Operator aritmatika: PLUS (`+`), MINUS (`-`), TIMES (`*`), DIVIDE (`/`)
   - Delimiter: LPAREN (`(`), RPAREN (`)`), COMMA (`,`)
   - Nilai dari `reserved`.
3. Buat aturan `t_NUMBER(t)` untuk mengonversi angka integer dan float (e.g. `10`, `3.14`).
4. Buat aturan `t_STRING`, `t_ID`, `t_newline`, `t_ignore`, dan `t_error`.
5. Jalankan lexer terhadap `DEFAULT_SOURCE` dan cetak tabel token lengkap
   (No, Line, Token Type, Lexeme / Value, Total Tokens).

Referensi aturan token lengkap dapat dilihat di `src/r_lexer.py` dan `README.md`.
=============================================================================
"""

import ply.lex as lex  # noqa: F401

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

# TODO (Athallah): Lengkapi definisi `reserved`, `tokens`, aturan `t_*`,
# serta fungsi utama untuk menjalankan lexer pada `DEFAULT_SOURCE`.
