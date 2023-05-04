from string import ascii_uppercase
class Solution:

    def unscramble(self, inputString, inputNumber):
        # Your code goes here
        n = len(ascii_uppercase)
        letter_to_number = dict(zip(ascii_uppercase, range(n)))
        number_to_letter = dict(zip(range(n),ascii_uppercase))
        return ''.join(list(map(lambda x: number_to_letter[(letter_to_number[x]-inputNumber)%n], inputString)))