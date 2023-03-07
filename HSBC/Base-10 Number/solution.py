import string 
digs = string.digits + string.ascii_uppercase

class Solution:

    def convert_base_ten(self, input_int, targetBase):
        # Your code goes here
        try:
            if int(input_int) != input_int or int(targetBase) != targetBase:
                return "INDETERMINATE"
            if targetBase == 0 or abs(targetBase) > len(digs):
                return "INDETERMINATE"
        except:
            return "INDETERMINATE"
        
        if targetBase < 0:
            return self.int2negbase(int(input_int), int(targetBase))
        else:
            return self.int2base(int(input_int), int(targetBase))
        
def int2base(self, input_int, targetBase):
        if input_int < 0:
            sign = -1
        elif input_int > 0:
            sign = 1 
        else:
            return digs[0]
        
        input_int *= sign
        digits = []
        
        while input_int:
            digits.append(digs[input_int % targetBase])
            input_int = input_int // targetBase
        
        if sign < 0:
            digits.append("-")
        digits.reverse()
        return ''.join(digits)
        
def int2negbase(self, input_int, targetBase):
        digits = []
        if input_int == 0:
            return digs[0]
        while input_int:
            input_int, remainder = divmod(input_int, targetBase)
            if remainder < 0:
                input_int, remainder = input_int+1,remainder-targetBase
            digits.append(digs[remainder])
            
        digits.reverse()
        return ''.join(digits)