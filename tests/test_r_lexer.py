# Unit Tests R-Like Lexer
# Group 2 - LD07

from pathlib import Path
import unittest

from src.r_lexer import tokenize_code


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_INPUTS = PROJECT_ROOT / "sample_inputs"


# Case validation specs
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

    # Check discovered sample files
    def test_all_discovered_sample_cases(self):
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

    # Test lexical error recovery
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
