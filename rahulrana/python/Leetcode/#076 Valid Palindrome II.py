# https://leetcode.com/problems/valid-palindrome-ii/submissions/

def palindromeCheck(lst):
    length = len(lst)
    for i in range(length//2):
        if lst[i] != lst[length-1-i]:
            return False
    return True
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if palindromeCheck(s) == True:
            return True
        s = list(s)
        length = len(s)
        for i in range(length//2):
            if s[i] != s[length-1-i]:
                temp = s[i]
                del s[i]
                if palindromeCheck(s) == True:
                    return True
                s.insert(i, temp)
                del s[length-1-i]
                if palindromeCheck(s) == True:
                    return True
                return False
        return False