# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 22:08:54 2021

@author: javia
"""

from solution import Cipher
import unittest

class CipherTests(unittest.TestCase):

    
    def test1(self):
        solution = Cipher()
        self.assertEqual(solution.split_string_on_change("TDpmfe&dcqs!@"), "T ,D ,p ,m ,f ,e ,& ,d ,c ,q ,s ,! ,@ ")

    def test2(self):
        solution = Cipher()
        self.assertEqual(solution.split_string_on_change("BEpk93diawcTW£!£"), "B ,E ,p ,k ,9 ,3 ,d ,i ,a ,w ,c ,T ,W ,£ ,! ,£ ")

if __name__ == '__main__':
    unittest.main()