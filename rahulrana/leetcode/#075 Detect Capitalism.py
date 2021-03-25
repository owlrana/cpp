# https://leetcode.com/problems/detect-capital/submissions/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lst = [word.upper(), word.lower(), word.capitalize()]
        if word in lst:
            return True
        return False