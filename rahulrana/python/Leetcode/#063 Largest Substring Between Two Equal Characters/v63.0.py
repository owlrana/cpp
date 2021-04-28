# https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def sameCharFinder(lst):
        one = -1
        two = -1
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[i] == lst[j] and abs(i - j) > abs(one - two):
                    one = i
                    two = j
        return (one, two)
    
    def maxLengthBetweenEqualCharacters(s: str) -> int:
        string = list(s)
        (a, b) = Solution.sameCharFinder(string)
        # subtracting - 1 because it will be counting the last index too
        if a == -1 or b == -1:
            return -1
        return abs(a - b) - 1
    
assert Solution.maxLengthBetweenEqualCharacters("cbzxy") == -1