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
