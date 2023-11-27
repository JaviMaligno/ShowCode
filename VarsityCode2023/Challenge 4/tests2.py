import unittest
from solution2 import find_balance_point

class TestSolution(unittest.TestCase):
    def test_find_balance_point(self):
        self.assertEqual(find_balance_point([2, 7, 4, 5, -3, 8, 9, -1]), 3)

if __name__ == '__main__':
    unittest.main()
