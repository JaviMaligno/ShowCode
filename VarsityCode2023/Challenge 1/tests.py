from solution import Trader
import unittest

class TraderTests(unittest.TestCase):

    
    def test1(self):
        result = Trader()
        self.assertEqual(result.fill_pattern([ 2, 1 ], [ "X.", ".X", "XX" ]), 2)

    def test2(self):
        result = Trader()
        self.assertEqual(result.fill_pattern([ 1, 3, 2 ], [ "XX.", ".XX", "X..", ".X.", "..X" ]), 3)

    def test3(self):
        result = Trader()
        self.assertEqual(result.fill_pattern([ 2, 3, 1, 1, 0, 0, 3, 2 ], [ "XXXX....", "XX......", "..XX....", "......XX", ".X......", "X......." ]), 15)

if __name__ == '__main__':
    unittest.main()