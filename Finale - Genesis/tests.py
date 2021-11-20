# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 20:51:47 2021

@author: javia
"""

from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.final_function(8), 18)

if __name__ == '__main__':
    unittest.main()