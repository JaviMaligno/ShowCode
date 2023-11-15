from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.simp([ 192, 900 ]), 92)

    def test2(self):
        result = Solution()
        self.assertEqual(result.simp([ 186, 200, 141, 200, 900 ]), 86)

    def test_NOP(self):
        result = Solution()
        program = [0, 900]
        self.assertEqual(result.simp(program), 0) 

    def test_MOV(self):
        result = Solution()
        program = [100, 900]
        self.assertEqual(result.simp(program), 0)

    def test_ADD(self):
        result = Solution()
        result = Solution()
        program = [100, 400, 900]
        self.assertEqual(result.simp(program), 0)

    def test_SUB(self):
        result = Solution()
        program = [105, 500, 900]
        self.assertEqual(result.simp(program), 5)

    def test_JMP(self):
        result = Solution()
        program = [701, 900]
        self.assertEqual(result.simp(program), 0)
    
    def test_JGT(self):
        result = Solution()
        program = [105, 802, 900]
        self.assertEqual(result.simp(program), 5)


    
  
if __name__ == '__main__':
    unittest.main()