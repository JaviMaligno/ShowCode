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

    def test5(self):
        result = Detector()
        self.assertEqual(result.count_decays([ 0,0,0,0,0]), 0)

    def test6(self):
        result = Detector()
        self.assertEqual(result.count_decays([ 3,3,3]), 0)

    def test7(self):
        result = Detector()
        self.assertEqual(result.count_decays([10,10,10,10,10,10,10,10,10,10,10,39.025841,48.913206,49.126453,44.969661,39.301081,33.569323,28.432154,24.120506,20.648415,17.93094,38.394688,44.503456,43.498161,39.405575,34.370599,29.459426,25.13767,21.550484,18.683248,16.451144,53.476429,65.387558,64.719562,58.472005,50.396429,42.377196,35.254882,29.309695,24.539601,20.815967,75.599555,93.085466,91.911926,82.481706,70.36648,58.361594,47.711083,38.826726,31.701582,26.141328,21.888562,18.685517,16.302277,14.546431,13.263332,12.33211,11.660211,11.177861,10.833107]),4)
    
    def test8(self):
        result = Detector()
        self.assertEqual(result.count_decays([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,28.221211,98.195129,121.933633,128.493342,178.768351,181.928239,163.574493,137.548896,110.904807,86.878728,66.640364,50.303614,37.495597,27.665229,20.241258,14.705453,10.619736,7.629658,5.456871,3.887473,2.759772]), 5)
if __name__ == '__main__':
    unittest.main()