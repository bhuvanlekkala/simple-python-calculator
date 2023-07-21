import unittest
from calculator import add_numbers

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(5, -3), 2)

if __name__ == '__main__':
    unittest.main()
