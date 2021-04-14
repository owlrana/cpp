# https://leetcode.com/problems/length-of-last-word/submissions/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        try:
            return len(words[len(words) - 1])
        except:
            return 0