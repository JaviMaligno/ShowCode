from fileinput import filename


class Solution:

    def handle_file(self, fileName):
        # Your code goes here
        fileName = self.reverse_brace(fileName)
        fileName = self.shift_bracket(fileName, brackets='()')
        fileName = self.shift_bracket(fileName, brackets='<>')
        fileName = fileName.replace('(', '').replace(')','').replace('<', '').replace('>','')
        return fileName

    def reverse_brace(self, fileName):
        braces = list(self.bracketing(fileName, brackets= "{}"))
        for (d, (start,end)) in braces:
            if d % 2:
                fileName = fileName[:start]+self.reverse(fileName[start:end])+fileName[end:]
        fileName = fileName.replace('{', '').replace('}','')
        return fileName

    
    def shift_bracket(self, fileName, brackets):
        braces = list(self.bracketing(fileName, brackets = brackets))
        s = -7 if brackets == '()' else 2
        for (d, (start,end)) in braces:
            shift = s*d
            shifted = self.caesar(fileName[start:end], shift)
            fileName = fileName[:start]+shifted+fileName[end:]
        return  fileName
    
    @staticmethod
    def bracketing(string, brackets = '()'):
        stack = []
        for i, c in enumerate(string):
            if c == brackets[0]:
                stack.append(i)
            elif c == brackets[1] and stack:
                start = stack.pop()
                yield (len(stack)+1,(start+1,i))
    
    @staticmethod
    def reverse(string):
        brackets = ['(', ')', '<', '>', '{', '}']
        listSample=list(string)
        i=0
        j=len(listSample)-1
 
        while i<j:
            if  listSample[i] in brackets:
                i+=1
            elif listSample[j] in brackets:
                j-=1
            else:
                #swap the element in the list 
                #if both elements are alphabets
                listSample[i], listSample[j]=listSample[j], listSample[i]
                i+=1
                j-=1
        strOut=''.join(listSample)
        return strOut
        
    @staticmethod
    def caesar(text, s):
        result = ''
        for i in range(len(text)):
            char = text[i]
            # Encrypt uppercase characters in plain text
            if char.isupper():
                result += chr((ord(char) + s-65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            elif char.islower():
                result += chr((ord(char) + s - 97) % 26 + 97)
            else:
                #Brackets return False in both
                result += char 
        return result


    




