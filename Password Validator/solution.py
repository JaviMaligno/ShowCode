# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 23:00:11 2021

@author: javia
"""
import re
#If I cannot import re (regex) then I will have to define the alphabet
class PasswordValidator:
    
    def __init__(self):
        self.special_characters=['-','@', '_', '+', '!', '?', '%', '$', '#']
        self.regex_special='['+''.join(self.special_characters)+']{2,}'

    def validate_password(self, userPassword):
        # Your code goes here
        
        
        #str.isalpha()
        #isdigit()
        #isalnum()
        #without () these thngs can still be used as booleans, but it is safer to use () because I've seen weird behaviour wihout it
        #print([x.isalpha() for x in u'Español-한국어'])
        if len(userPassword)>=12 and len(userPassword)<=25 \
            and 'password' not in userPassword \
            and any(c.isdigit() for c in userPassword) \
            and any(c in self.special_characters for c in userPassword) \
            and re.search('[A-Z]',userPassword) \
            and self.consecutive_special(userPassword) \
            and userPassword[-1] not in self.special_characters \
            and not userPassword[-1].isdigit() \
            and self.five_in_a_row(userPassword) \
            and all(userPassword.count(c)<4 for c in userPassword) \
            and self.no_other_characters(userPassword):
                return 'Pass'
        else:
            return 'Fail'
                
        
    def consecutive_special(self,password):
        #checks whether the password has two consecutive numbers or special characters, returns False if it does
        return not (re.search('[0-9][0-9]',password) or re.search(self.regex_special,password))
    
                    
    def five_in_a_row(self,password):
        #checks whether the password contains 5 letter in a row and returns if it doesn't and the password is less than 20 characters lon
        if len(password)>19:
            return True
        else:
            return re.search('[a-zA-Z]{5,}',password)
    
    def no_other_characters(self,password):
        return all(c.isalnum() or c in self.special_characters for c in password)