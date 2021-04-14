# https://leetcode.com/problems/reverse-only-letters/submissions/

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        string = list(S)
        length = len(string)
        j = length-1
        i = 0
        reverse_string = []
        while i in range(length):
            if (ord(string[i]) >= 65 and ord(string[i]) <= 90) or (ord(string[i]) >= 97 and ord(string[i]) <= 122):
                if (ord(string[j]) >= 65 and ord(string[j]) <= 90) or (ord(string[j]) >= 97 and ord(string[j]) <= 122):
                    reverse_string.append(string[j])
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                reverse_string.append(string[i])
                i += 1
        str1 = ''.join(str(e) for e in reverse_string)
        return str1