# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 21:47:44 2021

@author: javia
"""
class Cipher:

    def split_string_on_change(self, CipherString):
        # Your code goes here
        if not CipherString:
            return CipherString
        
        current_char=CipherString[0]
        current_string=''
        
        for i in CipherString:
              
            if i==current_char:
                current_string+=current_char#next(iter_string)
            else:
                current_char=i
                current_string+=' ,'+current_char#next(iter_string)
                
            
        return current_string+' '
    