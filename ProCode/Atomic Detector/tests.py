from solution import Detector
import unittest

class DetectorTests(unittest.TestCase):

    
    def test1(self):
        result = Detector()
        self.assertEqual(result.count_decays([ 0, 0, 0, 38.275869, 51.314164, 51.595369, 46.11388, 38.638823, 31.080453, 24.306159 ]), 1)

    def test2(self):
        result = Detector()
        self.assertEqual(result.count_decays([ 3, 3, 3, 57.906675, 76.61009, 77.013478, 69.150291, 58.427332, 47.584862, 65.66898, 66.983277, 60.619558, 51.49755, 42.127624, 33.664707, 26.529161, 20.765596, 16.244936, 12.774096, 10.152211 ]), 2)
   
    def test3(self):
        result = Detector()
        self.assertEqual(result.count_decays([ 3 ]), 0)

    def test4(self):
        result = Detector()
        self.assertGreater(result.count_decays([ 3, 10.152211 ]), 0)

if __name__ == '__main__':
    unittest.main()