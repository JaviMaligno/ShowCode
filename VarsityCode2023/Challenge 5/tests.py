from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        result = Solution()
        self.assertEqual(result.factorial(5), 120)

   
    def test2(self):
        result = Solution()
        self.assertEqual(result.print_fizz_buzz(15), "FizzBuzz")

  
    def test3_1(self):
        result = Solution()
        self.assertEqual(result.get_largest_number(3), 3)

    def test3_2(self):
        result = Solution()
        self.assertEqual(result.get_largest_number(36), 63)

if __name__ == '__main__':
    unittest.main()