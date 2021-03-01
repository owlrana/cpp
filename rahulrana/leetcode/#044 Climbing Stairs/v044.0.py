# https://leetcode.com/problems/climbing-stairs/submissions/

class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=1
        for i in range(n):
            temp = a
            a = b
            b += temp
        return a