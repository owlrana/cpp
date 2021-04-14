# https://leetcode.com/problems/make-the-string-great/submissions/

class Solution:
    def makeGood(self, s: str) -> str:
        length = len(s)
        s = list(s)
        i = 0
        while i <= length -2:
            if abs(ord(s[i]) - ord(s[i+1])) == 32:
                del s[i]
                del s[i]
                length -= 2
                if i != 0:
                    i -= 1
            else:
                i += 1
        string = "".join(element for element in s)
        return string