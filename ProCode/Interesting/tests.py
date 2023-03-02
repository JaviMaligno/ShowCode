from solution import MarketInterest
import unittest

class MarketInterestTests(unittest.TestCase):

    
    def test1(self):
        result = MarketInterest()
        self.assertEqual(result.maximum_value([ "1.12,10,C", "1.12,10,S" ]), 0)

    def test2(self):
        result = MarketInterest()
        self.assertEqual(result.maximum_value([ "1.12,10,S", "1.12,10,C" ]), 1)
    
    def test_simple_interest(self):
        result = MarketInterest()
        self.assertEqual(result.simple_interest(0.03,365), 11.95)
    
    def test_compound_interest(self):
        result = MarketInterest()
        self.assertEqual(round(result.compound_interest(0.03,365),2), 48482.72)
    
    def test_wrong_type(self):
        result = MarketInterest()
        self.assertEqual(result.interest(0.03,365, "H"), 0)
    
    def test_compound_wins(self):
        result = MarketInterest()
        self.assertGreater(result.interest(1.12,10,"C"), result.interest(1.12,10,"S"))



if __name__ == '__main__':
    unittest.main()