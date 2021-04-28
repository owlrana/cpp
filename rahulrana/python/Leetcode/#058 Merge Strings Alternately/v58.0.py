# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        low = min(len1, len2)
        remaining = abs(len1 - len2)
        new_word = []
        for i in range(low):
            new_word.append(word1[i])
            new_word.append(word2[i])
        if remaining:
            if len1 > len2:
                leftover = word1
            else:
                leftover = word2    
            for j in range(remaining):
                new_word.append(leftover[low+j])
        ret_word = "".join(str(element) for element in new_word)
        return ret_word