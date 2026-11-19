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


"""
Automated unit tests for the R-like lexical analyzer.

The sample-case specifications are kept in one table so each case can use the
same assertions and a new `case*_input.R` file can be covered with little code.
"""

from pathlib import Path
import unittest

from src.r_lexer import tokenize_code


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_INPUTS = PROJECT_ROOT / "sample_inputs"


CASE_SPECS = {
    "case1_input.R": {
        "required_types": (
            "PRINT", "LPAREN", "STRING", "RPAREN",
            "CAT", "LPAREN", "STRING", "RPAREN",
        ),
        "required_values": ("Hello, world!", "Thanks"),
        "exact_types": True,
    },
    "case2_input.R": {
        "required_types": ("ASSIGN", "PLUS", "DIVIDE", "NUMBER", "CAT"),
        "required_values": (),
    },
    "case3_input.R": {
        "required_types": ("IF", "ELSE", "GT", "LBRACE", "RBRACE", "SEMICOLON"),
        "required_values": (),
    },
    "case4_input.R": {
        "required_types": ("WHILE", "LE", "MODULO", "NE", "IF"),
        "required_values": (),
    },
}


class TestRLikeLexer(unittest.TestCase):
    def assert_valid_sample(self, filename):
        source_path = SAMPLE_INPUTS / filename
        self.assertTrue(source_path.is_file(), f"Missing sample input: {source_path}")

        source_code = source_path.read_text(encoding="utf-8")
        tokens, errors = tokenize_code(source_code)
        token_types = [token.token_type for token in tokens]
        token_values = [token.value for token in tokens]

        self.assertEqual(errors, [], f"Unexpected lexical errors in {filename}")
        self.assertTrue(tokens, f"No tokens produced for {filename}")

        spec = CASE_SPECS.get(filename, {})
        required_types = spec.get("required_types", ())
        for token_type in required_types:
            self.assertIn(token_type, token_types, f"{filename}: missing {token_type}")

        if spec.get("exact_types"):
            self.assertEqual(token_types, list(required_types))

        for value in spec.get("required_values", ()):
            self.assertIn(value, token_values, f"{filename}: missing value {value!r}")

    def test_case1_simple_statement(self):
        self.assert_valid_sample("case1_input.R")

    def test_case2_arithmetic_expression(self):
        self.assert_valid_sample("case2_input.R")

    def test_case3_conditional_if_block(self):
        self.assert_valid_sample("case3_input.R")

    def test_case4_looping_with_conditional_if(self):
        self.assert_valid_sample("case4_input.R")

    def test_all_discovered_sample_cases(self):
        """Any additional case*_input.R file is also checked, using the shared rules."""
        files = sorted(SAMPLE_INPUTS.glob("case*_input.R"))
        self.assertTrue(files, "No sample case files were found")

        for source_path in files:
            with self.subTest(case=source_path.name):
                self.assert_valid_sample(source_path.name)

    def test_comments_are_ignored(self):
        source_code = "# R version 3.4.4\nx <- 10"
        tokens, errors = tokenize_code(source_code)

        self.assertEqual(errors, [])
        self.assertNotIn("COMMENT", [token.token_type for token in tokens])

    def test_lexical_error_handling(self):
        source_code = "x <- 10\n@bad $next\nok <- 20"
        tokens, errors = tokenize_code(source_code)

        self.assertEqual(
            [(error.line, error.column, error.character) for error in errors],
            [(2, 1, "@"), (2, 6, "$")],
        )
        token_types = [token.token_type for token in tokens]
        token_values = [token.value for token in tokens]

        self.assertIn("ASSIGN", token_types)
        self.assertIn("NUMBER", token_types)
        self.assertIn("ok", token_values)
        self.assertIn("next", token_values)


if __name__ == "__main__":
    unittest.main()
