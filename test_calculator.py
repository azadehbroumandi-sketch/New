import subprocess
import sys
import unittest
from pathlib import Path

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

    def test_square_root(self):
        self.assertEqual(sqrt(9), 3.0)
        self.assertAlmostEqual(sqrt(2.25), 1.5)
        self.assertEqual(sqrt(0), 0.0)
        self.assertEqual(calculate(16, "sqrt"), 4.0)

    def test_square_root_of_negative_number(self):
        with self.assertRaises(ValueError):
            sqrt(-1)
        with self.assertRaises(ValueError):
            calculate(-1, "sqrt")

    def test_square_root_dispatch_and_validation(self):
        self.assertEqual(calculate(9, "sqrt"), 3.0)
        with self.assertRaises(ValueError):
            calculate(9, "sqrt", 1)
        with self.assertRaises(TypeError):
            sqrt(True)
        with self.assertRaises(TypeError):
            sqrt("9")

    def test_square_root_cli(self):
        calculator_path = Path(__file__).with_name("calculator.py")
        result = subprocess.run(
            [sys.executable, str(calculator_path), "9", "sqrt"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "3.0\n")

        invalid = subprocess.run(
            [sys.executable, str(calculator_path), "-1", "sqrt"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertNotEqual(invalid.returncode, 0)
        self.assertIn("cannot calculate the square root of a negative number", invalid.stderr)

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
