from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.unscramble("EPH", 1), "DOG")

    def test2(self):
        result = Solution()
        self.assertEqual(result.unscramble("KL", 3), "HI")

    def test3(self):
        result = Solution()
        self.assertEqual(result.unscramble("KIB", 8), "CAT")

    def test4(self):
        result = Solution()
        self.assertEqual(result.unscramble("A", 3), "X")

    def test5(self):
        result = Solution()
        self.assertEqual(result.unscramble("", 3), "")

if __name__ == '__main__':
    unittest.main()