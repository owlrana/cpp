# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    
    def counter(string, char):
        count = 0
        for element in string:
            if element == char:
                count += 1
        return count 
    
    def maxScore(s: str) -> int:
        n = len(s)
        divider = 0
        scores = []
        for i in range(n-1):
            left = s[:divider+1]
            right = s[divider+1: n]
            print(left)
            print(right)
            leftNum = Solution.counter(left, "0")
            rightNum = Solution.counter(right, "1")
            scores.append(leftNum + rightNum)
            divider +=1
        return max(scores)

assert Solution.maxScore("01") == 2