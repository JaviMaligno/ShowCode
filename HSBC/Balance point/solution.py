class Solution:

    def balance_point(self, array):
        # Your code goes here
        point = -1
        for i in range(len(array)):
            left_balance, right_balance = self.balance_values(array,i)
            if left_balance == right_balance:
                point = i
                break
        return point
            
        
    
    def balance_values(self, array, index):
        left_balance = sum(array[:index])
        right_balance = sum(array[index+1:])
        return left_balance, right_balance