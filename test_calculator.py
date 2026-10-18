import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 0), -1)
    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 2), 3)
        self.assertEqual(calculator.subtract(-1, -1), 0)
    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 4), 8)
        self.assertEqual(calculator.multiply(-3, 3), -9)
    def test_divide(self):
        self.assertEqual(calculator.divide(8, 2), 4)
        self.assertAlmostEqual(calculator.divide(7, 3), 7/3)
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
