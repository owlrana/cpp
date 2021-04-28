# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/submissions/

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        length = len(s)
        nums = [0]*26
        for i in range(length):
            nums[ord(s[i]) - ord('a')] += 1
            nums[ord(t[i]) - ord('a')] -= 1
        count = 0
        for num in nums:
            count += abs(num)
        return count//2