import unittest

from calculator import add, calculate, divide, multiply, subtract


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
