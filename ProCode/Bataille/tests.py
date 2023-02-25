from solution import Bataille
import unittest

class BatailleTests(unittest.TestCase):

    
    def test1(self):
        result = Bataille()
        self.assertEqual(result.play("2A", "2K"), 0)

    def test2(self):
        result = Bataille()
        self.assertEqual(result.play("A2QK", "457JT"), 1)
    
    def test3(self):
        result = Bataille()
        self.assertEqual(result.play("K2A", "K56"), 1)

    def test2a(self):
        result = Bataille()
        self.assertEqual(result.play("457JT","A2QK"), 2)
    
    def test3a(self):
        result = Bataille()
        self.assertEqual(result.play("K56", "K2A"), 2)

    def test1a(self):
        result = Bataille()
        self.assertEqual(result.play("", "2K"), 2)

    def test1b(self):
        result = Bataille()
        self.assertEqual(result.play("2A", ""), 1)
    
    def test1c(self):
        result = Bataille()
        self.assertEqual(result.play("", ""), 0)
    
    def test1c(self):
        result = Bataille()
        self.assertEqual(result.play("K", "234"), 1)
if __name__ == '__main__':
    unittest.main()