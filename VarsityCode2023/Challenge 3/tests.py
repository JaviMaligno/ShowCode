import unittest
from solution import rotThirteen

class TestSolution(unittest.TestCase):
    def test_rotThirteen(self):
        self.assertEqual(rotThirteen("Hello world"), "Uryyb jbeyq")
        self.assertEqual(rotThirteen("Goodbye world"), "Tbbqolr jbeyq")

if __name__ == '__main__':
    unittest.main()
