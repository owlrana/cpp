# https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed_list = list(allowed)
        words_list = list(words)
        count = 0
        for word in words_list:
            flag = True
            for char in word:
                if char not in allowed_list:
                    flag = False
            if flag == True:
                count += 1 
        return count