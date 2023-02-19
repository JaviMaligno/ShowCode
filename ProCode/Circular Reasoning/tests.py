from solution import Network
import unittest

class NetworkTests(unittest.TestCase):

    
    def test1(self):
        result = Network()
        self.assertEqual(result.nodes_visited(12, 3, [ 10 ]), 7)

    def test2(self):
        result = Network()
        self.assertEqual(result.nodes_visited(4, 4, [ 2, 4 ]), 4)

    def test3(self):
        result = Network()
        self.assertEqual(result.nodes_visited(4, 4, [ ]), 0)
    
    def test4(self):
        result = Network()
        self.assertEqual(result.nodes_visited(0, 4, [ 2, 4 ]), 0)
    
    def test5(self):
        result = Network()
        self.assertEqual(result.nodes_visited(4, 5, [ 2, 4 ]), 0)

    def test6(self):
        result = Network()
        self.assertEqual(result.nodes_visited(4, 4, [ 4 ]), 1)
    
    def test7(self):
        result = Network()
        self.assertEqual(result.nodes_visited(4, 2, [ 4,3]), 4)
    
    def test8(self):
        result = Network()
        self.assertEqual(result.nodes_visited(4, 4, [ 4,3 ]), 4)

    def test9(self):
        result = Network()
        self.assertEqual(result.nodes_visited(4, 3, [ 2,4 ]), 4)

    def test1(self):
        result = Network()
        self.assertEqual(result.nodes_visited(12, 3, [ 10, 1 ]), 10)

if __name__ == '__main__':
    unittest.main()