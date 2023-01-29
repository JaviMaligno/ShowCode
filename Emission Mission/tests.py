from solution import BAE_Emissions
import unittest

class BAE_EmissionsTests(unittest.TestCase):

    
    def test1(self):
        result = BAE_Emissions()
        self.assertEqual(result.forecast([ "09-17;3" ], [ 0, 0, 0, 0, 1, 0, 1, 2, 1, 2, 0, 1, 1, 3, 2, 2, 3, 2, 1, 1, 0, 1, 2, 4 ]), 10)

    def test2(self):
        result = BAE_Emissions()
        self.assertEqual(result.forecast([ "10,12;5", "11-13;6" ], [ 1, 1, 2, 0, 1, 0, 1, 2, 4, 2, 5, 3, 4, 3, 2, 2, 3, 2, 1, 1, 3, 2, 1, 0 ]), 10)

if __name__ == '__main__':
    unittest.main()