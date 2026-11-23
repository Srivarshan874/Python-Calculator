import unittest

import calculator


class CalculatorTests(unittest.TestCase):
    def test_arithmetic(self):
        self.assertEqual(calculator.add(8, 2), 10)
        self.assertEqual(calculator.subtract(8, 2), 6)
        self.assertEqual(calculator.multiply(8, 2), 16)
        self.assertEqual(calculator.divide(8, 2), 4)

    def test_division_by_zero(self):
        self.assertEqual(calculator.divide(8, 0), "Cannot divide by zero.")

    def test_unit_conversions(self):
        self.assertAlmostEqual(calculator.kilometres_to_miles(10), 6.21371)
        self.assertAlmostEqual(calculator.celsius_to_fahrenheit(25), 77)
        self.assertAlmostEqual(calculator.kilograms_to_pounds(10), 22.0462)


if __name__ == "__main__":
    unittest.main()
