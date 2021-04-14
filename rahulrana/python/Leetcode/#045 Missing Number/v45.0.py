# https://leetcode.com/problems/missing-number/submissions/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        sum1 = (n*(n-1))/2
        sum2 = sum(nums)
        return int(sum1 - sum2)