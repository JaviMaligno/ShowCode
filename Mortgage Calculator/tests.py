from solution import MortgageCalculator
import unittest

class MortgageCalculatorTests(unittest.TestCase):

    
    def test1(self):
        result = MortgageCalculator()
        self.assertEqual(result.calculate_eligibility(2, 400000, 20000, 38000, 45000, 0), [ 0, 0, 0, 0 ])

    def test2(self):
        result = MortgageCalculator()
        self.assertEqual(result.calculate_eligibility(1,120000, 18000, 29000, 0, 0), [ 145000, 11635.18, 232703.5, 20 ])

    def test5(self):
        result = MortgageCalculator()
        self.assertEqual(result.calculate_eligibility(1, 120000, 18000, 29000, 0, 2000), [ 145000, 11635.18, 232703.5, 18 ])

if __name__ == '__main__':
    unittest.main()