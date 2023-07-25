import unittest
import utility

class UtilityTestCase(unittest.TestCase):

    def test_multiply(self):
        result = utility.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = utility.divide(6, 3)
        self.assertEqual(result, 2)

    def test_max(self):
        result = utility.max()
        self.assertEqual(result, "oops")

if __name__ == '__main__':
    unittest.main()
