from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.find_path("HHHHHH\n....D.\n.D....\n...D..\nD.....\n.....D"), [ 2 ])

    def test2(self):
        result = Solution()
        self.assertEqual(result.find_path("HHHHH\n.....\n.....\n.....\n.....\n....."), [ 0, 1, 2, 3, 4 ])

    def test3(self):
        result = Solution()
        self.assertEqual(result.find_path("HHHHH\n.D.D.\n..D..\n....D\n.....\n....."), [ 0 ])
    
    def test4(self):
        result = Solution()
        self.assertEqual(result.find_path("HHHHH"), [ 0,1,2,3,4 ])

if __name__ == '__main__':
    unittest.main()