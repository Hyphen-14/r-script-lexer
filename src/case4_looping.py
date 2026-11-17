"""
=============================================================================
Compilation Technique (Class LD07) - Group Assignment Project 1
Lexical Analyzer Development using Python PLY

Group : Group 2 — R-Like Scripting
Case  : 4. Simple Looping with Conditional IF Block (Slide 20)
PIC   : 2802515261 - Early Achiril Putra

Members:
  1. 2802438754 - Nathasa Bintang Kayesa
  2. 2802495051 - Yasin Taryaqil Aghyar
  3. 2802521932 - Athallah Rafif Rijal Belvana
  4. 2802431395 - Samuel Tristan Ryansyah
  5. 2802515261 - Early Achiril Putra
=============================================================================

PETUNJUK PENGERJAAN (KASUS 4 — SIMPLE LOOPING WITH CONDITIONAL IF BLOCK):
------------------------------------------------------------------------
Target Input Source Code (Slide 20 / sample_inputs/case4_input.R):
    #R version 3.4.4 
    cat("List of Odd Number 1-100: \\n")
    num<-1
    while (num <= 100) {
    sisa <- (num %% 2) 
    if (sisa != 0) {
    oddnum <- num
    cat(oddnum," ");
    }
    num <- num + 1 
    }

Yang perlu diimplementasikan menggunakan `ply.lex`:
1. Definisikan `reserved`:
   - "while" -> "WHILE", "if" -> "IF", "else" -> "ELSE", "cat" -> "CAT", "print" -> "PRINT".
2. Definisikan `tokens`:
   - ID, NUMBER, STRING, ASSIGN (`<-`), MODULO (`%%`)
   - Operator aritmatika: PLUS, MINUS, TIMES, DIVIDE
   - Operator relasional: LE (`<=`), GE (`>=`), EQ (`==`), NE (`!=`), LT (`<`), GT (`>`)
   - Delimiter: LPAREN, RPAREN, LBRACE, RBRACE, COMMA, SEMICOLON
   - Nilai dari `reserved`.
3. Perhatikan token khusus di Kasus 4:
   - `t_MODULO = r"%%"` untuk operasi modulo khas bahasa R (`num %% 2`).
   - `t_LE = r"<="` untuk kondisi perulangan (`num <= 100`).
   - `t_NE = r"!="` untuk kondisi ganjil (`sisa != 0`).
4. Lengkapi `t_COMMENT`, `t_STRING`, `t_NUMBER`, `t_ID`, `t_newline`, `t_ignore`, dan `t_error`.
5. Jalankan lexer terhadap `DEFAULT_SOURCE` dan cetak tabel token lengkap.

Referensi aturan token lengkap dapat dilihat di `src/r_lexer.py` dan `README.md`.
=============================================================================
"""

import ply.lex as lex  # noqa: F401

DEFAULT_SOURCE = """#R version 3.4.4 
cat("List of Odd Number 1-100: \\n")
num<-1
while (num <= 100) {
sisa <- (num %% 2) 
if (sisa != 0) {
oddnum <- num
cat(oddnum," ");
}
num <- num + 1 
}
"""

# TODO (Early): Lengkapi definisi `reserved`, `tokens`, aturan `t_*`,
# serta fungsi utama untuk menjalankan lexer pada `DEFAULT_SOURCE`.
