# https://leetcode.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        string = list(S)
        length = len(string)
        j = length-1
        i = 0
        if length%2 == 0:
            loop = (length//2)
        else:
            loop = (length//2)
            
        while i in range(loop):
            if (ord(string[i]) >= 65 and ord(string[i]) <= 90) or (ord(string[i]) >= 97 and ord(string[i]) <= 122):
                if (ord(string[j]) >= 65 and ord(string[j]) <= 90) or (ord(string[j]) >= 97 and ord(string[j]) <= 122):
                    temp = string[i]
                    string[i] = string[j]
                    string[j] = temp
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                i += 1
        
        str1 = ''.join(str(e) for e in string)
        return str1