from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.filter_letters("aaabbabcddcc"), 15)

    def test2(self):
        result = Solution()
        self.assertEqual(result.filter_letters("aabbccddee"), 0)

    def test3(self):
        result = Solution()
        self.assertEqual(result.filter_letters("ddd"), 0)

    def test4(self):
        result = Solution()
        self.assertEqual(result.filter_letters(""), 0)

    def test5(self):
        result = Solution()
        self.assertEqual(result.filter_letters("za"), 27)

if __name__ == '__main__':
    unittest.main()