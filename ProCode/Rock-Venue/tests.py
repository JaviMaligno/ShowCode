from solution import Seating
import unittest

class SeatingTests(unittest.TestCase):

    
    def test1(self):
        result = Seating()
        self.assertEqual(result.largest_block([ "XXa222Ob" ]), "2")

    def test2(self):
        result = Seating()
        self.assertEqual(result.largest_block([ "acbccX", "fcbaOc", "ffbacc" ]), "b")
    
    def test3(self):
        result = Seating()
        self.assertEqual(result.largest_block([ [ 1, 4, 4, 4, 4, 3, 3, 1 ],
                        [ 2, 1, 1, 4, 3, 3, 1, 1 ],
                        [ 3, 2, 1, 1, 2, 3, 2, 1 ],
                        [ 3, 3, 2, 1, 2, 2, 2, 2 ],
                        [ 3, 1, 3, 1, 1, 4, 4, 4 ],
                        [ 1, 1, 3, 1, 1, 4, 4, 4 ] ]), 1)
        
    def test4(self):
        result = Seating()
        self.assertEqual(result.largest_block([ [ 1, 4, 4, 4, 4, 4, 4, 1 ],
                        [ 3, 3, 3, 3, 3, 3, 1, 1 ],]), 4)
    
    def test5(self):
        result = Seating()
        self.assertEqual(result.largest_block([ [ 1, "X", "X", "X", "X", "X", "X", 1 ],
                        [ 3, 3, 3, 3, 3, 1, 1, 1 ],]), 3)
    def test6(self):
        result = Seating()
        self.assertEqual(result.largest_block([ [ 1, "O", "O", "O", "O", "O", "O", 1 ],
                        [ 3, 3, 3, 3, 3, 1, 1, 1 ],]), 3)
    def test7(self):
        result = Seating()
        self.assertEqual(result.largest_block([ [ 1, "O", "O", "O", "O", "O", "O", 1 ],
                        [ "X", "X", "X", "X", "X", 1, 1, 1 ],]), 1)
    
    def test8(self):
        result = Seating()
        self.assertEqual(result.largest_block([ [ 1, "X", "X", "X", "X", "X", "X", 1 ],
                        [ "O", "O", "O", "O", "O", 1, 1, 1 ],]), 1)
        
    def test9(self):
        result = Seating()
        self.assertEqual(result.largest_block([ [ 1, 1, 1 ],
                        [  1, 1, 1 ],]), 1)
    
    def test10(self):
        result = Seating()
        self.assertEqual(result.largest_block([ [ "X", "X", "X","X" ],
                        [  "O", "O", "O", "X"],]), "O")

if __name__ == '__main__':
    unittest.main()