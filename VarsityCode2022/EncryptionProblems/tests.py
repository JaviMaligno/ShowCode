from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.handle_file("(o)(l)(s)(s)(v).(a)(e)(a)"), "hello.txt")

    def test2(self):
        result = Solution()
        self.assertEqual(result.handle_file("<l><m><b><c>.<h><q>"), "node.js")

    def test3(self):
        result = Solution()
        self.assertEqual(result.handle_file("<l><m><b><c>.{<q><h>}"), "node.js")

    def test4(self):
        result = Solution()
        self.assertEqual(result.handle_file("(<l>)<m><b><c>.{<q><h>}"), "gode.js")
if __name__ == '__main__':
    unittest.main()