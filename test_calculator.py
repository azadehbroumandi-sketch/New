import subprocess
import sys
import unittest

from calculator import add, calculate, divide, multiply, sqrt, subtract


class CalculatorTests(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(subtract(7, 4), 3)
        self.assertEqual(multiply(6, 5), 30)
        self.assertEqual(divide(8, 2), 4)

    def test_negative_and_decimal_values(self):
        self.assertAlmostEqual(add(-1.5, 0.5), -1.0)
        self.assertAlmostEqual(subtract(-2.5, 1.5), -4.0)
        self.assertAlmostEqual(multiply(-1.5, 2), -3.0)
        self.assertAlmostEqual(divide(-7.5, 2.5), -3.0)

    def test_square_root_of_integer(self):
        self.assertEqual(sqrt(81), 9.0)

    def test_square_root_operation_of_integer(self):
        self.assertEqual(calculate(81, "sqrt"), 9.0)

    def test_square_root_operation_of_decimal(self):
        self.assertAlmostEqual(calculate(2.25, "sqrt"), 1.5)

    def test_square_root_of_decimal(self):
        self.assertAlmostEqual(sqrt(2.25), 1.5)

    def test_square_root_of_negative_number(self):
        with self.assertRaises(ValueError):
            sqrt(-1)
        with self.assertRaises(ValueError):
            calculate(-1, "sqrt")

    def test_square_root_rejects_invalid_operands(self):
        with self.assertRaises(TypeError):
            calculate("9", "sqrt")
        with self.assertRaises(ValueError):
            calculate(9, "sqrt", 3)

    def test_square_root_cli_operation(self):
        result = subprocess.run(
            [sys.executable, "calculator.py", "9", "sqrt"],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.stdout.strip(), "3.0")

    def test_square_root_cli_rejects_negative_number(self):
        result = subprocess.run(
            [sys.executable, "calculator.py", "-1", "sqrt"],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("cannot take the square root", result.stderr)

    def test_binary_cli_operation_requires_right_operand(self):
        result = subprocess.run(
            [sys.executable, "calculator.py", "9", "+"],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("another number", result.stderr)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate(1, "%", 2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
        with self.assertRaises(ZeroDivisionError):
            calculate(10, "/", 0)

    def test_non_numeric_operands(self):
        with self.assertRaises(TypeError):
            add("1", 2)


if __name__ == "__main__":
    unittest.main()
