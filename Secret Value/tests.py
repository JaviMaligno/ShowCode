# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 16:27:09 2021

@author: javia
"""

from solution import Solution
import unittest

class SolutionTests(unittest.TestCase):

    
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.secret_value([ 1, 2, 5, 8, 11, 12 ], 5), "2")

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.secret_value([ 2, 7, 9, 13, 18, 22, 31 ], 14), "-1")

if __name__ == '__main__':
    unittest.main()