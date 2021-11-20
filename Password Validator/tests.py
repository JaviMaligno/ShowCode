# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 15:28:34 2021

@author: javia
"""

from solution import PasswordValidator
import unittest

class PasswordValidatorTests(unittest.TestCase):

    
    def test1(self):
        solution = PasswordValidator()
        self.assertEqual(solution.validate_password("This is my password!"), "Fail")

    def test2(self):
        solution = PasswordValidator()
        self.assertEqual(solution.validate_password("vwZoL#MH2jQTyKm"), "Pass")

if __name__ == '__main__':
    unittest.main()