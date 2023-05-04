from string import ascii_lowercase
class Solution:

    def filter_letters(self, message):
        # Your code goes here
        values = dict(zip(ascii_lowercase, range(1,len(ascii_lowercase)+1)))
        message = message.lower()
        letters = set(message)
        integer = 0
        if len(letters) <= 1:
            return integer
        for l in letters:
            times = message.count(l) 
            integer+=values[l]*times if times % 2 else 0
        return integer
        