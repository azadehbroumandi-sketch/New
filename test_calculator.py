import contextlib
import io
import unittest

from calculator import add, divide, main, multiply, subtract, validate_number


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(subtract(7, 4), 3)

    def test_multiplication(self):
        self.assertEqual(multiply(6, 5), 30)

    def test_division(self):
        self.assertEqual(divide(8, 2), 4)

    def test_numeric_strings_are_accepted(self):
        self.assertEqual(add("1.5", "2.5"), 4)

    def test_invalid_input_raises_value_error(self):
        for value in ("not a number", "", None, True, float("nan")):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    validate_number(value)

    def test_division_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_non_finite_values_are_rejected(self):
        for value in (float("inf"), float("-inf")):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    add(value, 1)

    def test_overflowing_integer_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_number(10 ** 400)

    def test_cli_prints_result(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = main(["multiply", "6", "7"])
        self.assertEqual(status, 0)
        self.assertEqual(output.getvalue(), "42.0\n")

    def test_cli_reports_invalid_arguments(self):
        error = io.StringIO()
        with contextlib.redirect_stderr(error):
            status = main(["unknown", "1", "2"])
        self.assertEqual(status, 2)
        self.assertIn("Usage:", error.getvalue())

    def test_cli_reports_calculation_errors(self):
        error = io.StringIO()
        with contextlib.redirect_stderr(error):
            status = main(["divide", "10", "0"])
        self.assertEqual(status, 1)
        self.assertIn("cannot divide by zero", error.getvalue())


if __name__ == "__main__":
    unittest.main()
