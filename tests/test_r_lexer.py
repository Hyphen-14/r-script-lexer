"""
=============================================================================
Compilation Technique (Class LD07) - Group Assignment Project 1
Automated Unit Tests for Group 2 — R-Like Scripting Lexical Analyzer

PIC : 2802515261 - Early Achiril Putra

PETUNJUK PENGERJAAN (UNIT TESTING & ERROR HANDLING):
----------------------------------------------------
Gunakan modul bawaan Python `unittest` untuk memverifikasi akurasi lexer
pada seluruh kasus (Kasus 1 s/d Kasus 4) dan skenario error leksikal.

Skenario pengujian yang disarankan:
1. `test_case1_simple_statement`:
   Uji `sample_inputs/case1_input.R` -> pastikan menghasilkan 8 token
   (`PRINT`, `LPAREN`, `STRING`, `RPAREN`, `CAT`, `LPAREN`, `STRING`, `RPAREN`)
   dengan 0 error dan string `'Thanks'` terbaca benar meski memakai smart quote `“`.
2. `test_case2_arithmetic_expression`:
   Uji `sample_inputs/case2_input.R` -> pastikan token `ASSIGN` (`<-`), `PLUS` (`+`),
   `DIVIDE` (`/`), `NUMBER`, dan `CAT` dikenali tanpa error.
3. `test_case3_conditional_if_block`:
   Uji `sample_inputs/case3_input.R` -> pastikan komentar `#R version 3.4.4`
   diabaikan dan token `IF`, `ELSE`, `GT`, `LBRACE`, `RBRACE`, `SEMICOLON` muncul.
4. `test_case4_looping_with_conditional_if`:
   Uji `sample_inputs/case4_input.R` -> pastikan `WHILE`, `LE` (`<=`), `MODULO` (`%%`),
   `NE` (`!=`), dan nested `IF` dikenali.
5. `test_lexical_error_handling`:
   Uji input dengan karakter ilegal (misalnya `@` atau `$`) dan pastikan
   `tokenize_code(...)` mencatat error pada baris & kolom yang tepat sambil tetap
   melanjutkan pemindaian token valid berikutnya.

Jalankan test dengan perintah:
    python -m unittest discover -s tests -p "test_*.py" -v
=============================================================================
"""

import unittest  # noqa: F401
from src.r_lexer import tokenize_code  # noqa: F401

# TODO (Early): Implementasikan class `TestRLikeLexer(unittest.TestCase)` di sini.
