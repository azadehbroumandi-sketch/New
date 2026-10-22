import math
import unittest

from sqrt import sqrt


class SqrtTests(unittest.TestCase):
    def test_square_root_of_positive_number(self):
        self.assertEqual(sqrt(9), 3.0)
        self.assertAlmostEqual(sqrt(2), math.sqrt(2))

    def test_square_root_of_zero(self):
        self.assertEqual(sqrt(0), 0.0)

    def test_square_root_of_fractional_number(self):
        self.assertAlmostEqual(sqrt(0.25), 0.5)

    def test_negative_number_raises_value_error(self):
        with self.assertRaises(ValueError):
            sqrt(-1)

    def test_non_numeric_value_raises_type_error(self):
        for value in ("9", None, [], 1 + 2j):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    sqrt(value)

    def test_boolean_is_not_accepted_as_a_number(self):
        with self.assertRaises(TypeError):
            sqrt(True)

    def test_infinity_and_nan_follow_math_sqrt_behavior(self):
        self.assertEqual(sqrt(math.inf), math.inf)
        self.assertTrue(math.isnan(sqrt(math.nan)))

    def test_negative_zero_is_accepted_and_preserves_zero_result(self):
        result = sqrt(-0.0)
        self.assertEqual(result, 0.0)
        self.assertEqual(math.copysign(1.0, result), 1.0)

    def test_errors_have_the_documented_messages(self):
        with self.assertRaisesRegex(ValueError, r"^sqrt\(\) is undefined for negative numbers$"):
            sqrt(-1)
        with self.assertRaisesRegex(TypeError, r"^sqrt\(\) requires a real number$"):
            sqrt("9")


if __name__ == "__main__":
    unittest.main()
