class Solution:

    def factorial(self, n):
        # Your code goes here
        result = 1
        for i in range(1,n+1):
            result *= i 
        return result
    

    def print_fizz_buzz(self, n):
        # Your code goes here
        if n % 3 == 0 and n % 5 == 0:
            return "FizzBuzz"
        elif n % 3 == 0:
            return "Fizz"
        elif n % 5 == 0:
            return "Buzz"
        else:
            return str(n)



    def get_largest_number(self, n):
        # Your code goes here
        digits = list(str(abs(n)))
        digits.sort(reverse=True)
        largest = int(''.join(digits))
        return largest if largest <= 2**31-1 else 2**31-1