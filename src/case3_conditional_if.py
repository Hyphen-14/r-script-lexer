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

import ply.lex as lex  # noqa: F401

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

# TODO (Samuel): Lengkapi definisi `reserved`, `tokens`, aturan `t_*`,
# serta fungsi utama untuk menjalankan lexer pada `DEFAULT_SOURCE`.
