from solution import main
import unittest

class mainTests(unittest.TestCase):

    
    def test1(self):
        result = main()
        self.assertEqual(result.altitude_change([ 100, 101, 102, 103 ]), [ 3, 0 ])

    def test2(self):
        result = main()
        self.assertEqual(result.altitude_change([ 100, 99, 98, 97 ]), [ 0, -3 ])

    def test3(self):
        result = main()
        self.assertEqual(result.altitude_change([ 100, 100, 100, 100 ]), [ 0, 0 ])

    def test4(self):
        result = main()
        self.assertEqual(result.altitude_change([ 100, 102, 104, 102, 104, 103 ]), [ 6, -3 ])

if __name__ == '__main__':
    unittest.main()