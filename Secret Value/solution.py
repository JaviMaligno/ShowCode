# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 22:25:47 2021

@author: javia
"""

class Solution:

    def secret_value(self, SortedArray, SecretValue):
        # Your code goes here
        if sorted(SortedArray)==SortedArray and SecretValue>0 and SecretValue<1+10**5:
            return self.binary_search(SortedArray,0,len(SortedArray)-1,SecretValue)
        else:
            return '-1'
    def binary_search(self,arr, low, high, x):
 
        if high >= low:
 
            mid = (high + low) // 2
 
       
            if arr[mid] == x:
                return str(mid)
 
    
            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x)
 
    
            else:
                return self.binary_search(arr, mid + 1, high, x)
 
        else:
   
            return '-1'