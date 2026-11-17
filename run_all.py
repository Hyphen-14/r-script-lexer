"""
=============================================================================
Compilation Technique (Class LD07) - Group Assignment Project 1
Master CLI Runner for Group 2 — R-Like Scripting Lexical Analyzer

PIC : 2802521932 - Athallah Rafif Rijal Belvana

PETUNJUK PENGERJAAN (CLI RUNNER):
---------------------------------
File ini digunakan untuk mengeksekusi seluruh 4 file sampel di `sample_inputs/`
secara berurutan atau file `.R` tertentu lewat argumen `--file`.

Langkah yang disarankan:
1. Impor helper yang sudah tersedia di `src/r_lexer.py`:
   `from src.r_lexer import format_token_table, tokenize_code`
2. Definisikan daftar `SAMPLE_CASES` untuk:
   - `sample_inputs/case1_input.R`
   - `sample_inputs/case2_input.R`
   - `sample_inputs/case3_input.R`
   - `sample_inputs/case4_input.R`
3. Gunakan `argparse` untuk mendukung opsi `--file <path>`.
4. Baca isi file dengan `encoding="utf-8"`, lalu panggil `format_token_table(...)`
   dan tampilkan ringkasan Total Tokens & Total Errors.
=============================================================================
"""

# TODO (Athallah): Implementasikan CLI runner menggunakan `src.r_lexer`.
