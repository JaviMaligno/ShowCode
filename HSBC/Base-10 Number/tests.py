from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.convert_base_ten(15, 16), "F")

    def test2(self):
        result = Solution()
        self.assertEqual(result.convert_base_ten(23, 8), "27")
        
    def test3(self):
        result = Solution()
        self.assertEqual(result.convert_base_ten(1000, -3), '2212001')
    
    def test4(self):
        result = Solution()
        self.assertEqual(result.convert_base_ten(-15, -10), '25')
        
    def test5(self):
        result = Solution()
        self.assertEqual(result.convert_base_ten(-15, 49), 'INDETERMINATE')
        
    def test5(self):
        result = Solution()
        self.assertEqual(result.convert_base_ten(-15.5, 9), 'INDETERMINATE')
        
    def test5(self):
        result = Solution()
        self.assertEqual(result.convert_base_ten(15.0, 16), 'F')
        
    def test5(self):
        result = Solution()
        self.assertEqual(result.convert_base_ten(15, 16.0), 'F')
    
    def test5(self):
        result = Solution()
        self.assertEqual(result.convert_base_ten("a", 9), 'INDETERMINATE')
        
    def test5(self):
        result = Solution()
        self.assertEqual(result.convert_base_ten(-15.5, "a"), 'INDETERMINATE')

if __name__ == '__main__':
    unittest.main()