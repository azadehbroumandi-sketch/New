import unittest

from calculator import (
    add,
    calculate_expression,
    divide,
    evaluate_expression,
    multiply,
    subtract,
)


class CalculatorOperationsTests(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(subtract(9, 4), 5)
        self.assertEqual(multiply(6, 7), 42)
        self.assertEqual(divide(9, 2), 4.5)

    def test_decimal_values(self):
        self.assertAlmostEqual(add(1.25, 2.5), 3.75)
        self.assertAlmostEqual(multiply(0.5, 1.2), 0.6)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_invalid_operands(self):
        with self.assertRaises(TypeError):
            add("2", 3)


class ExpressionTests(unittest.TestCase):
    def test_sample_expressions(self):
        self.assertEqual(evaluate_expression("2 + 3 * 4"), 14)
        self.assertEqual(evaluate_expression("(10 - 4) / 2"), 3)
        self.assertEqual(evaluate_expression("-2 + 0.5"), -1.5)

    def test_longer_alias_matches_main_function(self):
        self.assertEqual(calculate_expression("8 / 2 + 1"), 5)

    def test_expression_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate_expression("4 / (2 - 2)")

    def test_invalid_expression(self):
        for expression in ("", "2 ** 3", "hello", "2 +", "__import__('os')"):
            with self.subTest(expression=expression):
                with self.assertRaises(ValueError):
                    evaluate_expression(expression)


if __name__ == "__main__":
    unittest.main()
