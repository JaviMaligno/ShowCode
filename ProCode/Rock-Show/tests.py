from solution import Performance
import unittest

class PerformanceTests(unittest.TestCase):

    
    def test1(self):
        result = Performance()
        self.assertEqual(result.adjust([ 3, 1, 3, 20, 34, 10 ], [ 1, 9, 8, 2, 20, 30 ], 0, -1, 0, 0), 0)

    def test2(self):
        result = Performance()
        self.assertEqual(result.adjust([ 1, 2, 3, 4 ], [ 1, 2, 3, 4 ], 0, 0, 0, 0.001), 10)

if __name__ == '__main__':
    unittest.main()