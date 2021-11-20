# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 20:10:10 2021

@author: javia
"""
from math import prod 

class Solution:

    def final_function(self, input):
        # Your code goes here
        if input <2: #only 1 has no set of at least 2 positive addends, since for every other positive integer we have n=1+...+1 n times 
            return 0
        else:
            return self.product_partition(input)
            
    #returns a set of partitions, i.e., sequences of positive integers that add up to input     
    def partitions(self,input):
        partition = set()
        partition.add((input, ))
        for x in range(1, input):
            for y in self.partitions(input - x):
                partition.add(tuple(sorted((x, ) + y)))
        return partition
            
    
    def product_partition(self,input):
        products=set()
        for p in self.partitions(input):
            products.add(prod(p))
        return max(products)