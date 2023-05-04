from solution import main
import unittest

class mainTests(unittest.TestCase):

    
    def test1(self):
        result = main()
        self.assertEqual(result.find_password("aaa12a3aaa4aa"), "1234")

    def test2(self):
        result = main()
        self.assertEqual(result.find_password("aaahi"), "hi")

if __name__ == '__main__':
    unittest.main()