from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    def test1(self):
        result = Solution()
        self.assertEqual(result.balance_point([ 2, 7, 4, 5, -3, 8, 9, -1 ]), 3)

    def test2(self):
        result = Solution()
        self.assertEqual(result.balance_point([-1,2 ]), -1)

    def test3(self):
        result = Solution()
        self.assertEqual(result.balance_point([-1]), 0)

    def test4(self):
        result = Solution()
        self.assertEqual(result.balance_point([-1,1,-1]), 0)
    
    def test5(self):
        result = Solution()
        self.assertEqual(result.balance_point([]), -1)

if __name__ == '__main__':
    unittest.main()