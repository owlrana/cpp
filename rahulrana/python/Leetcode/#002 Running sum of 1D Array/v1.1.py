# Leetcode: https://leetcode.com/problems/running-sum-of-1d-array/submissions/

class Solution:
    def runningSum(self, nums) :
        nums_sum = []
        current_sum = 0
        for item in nums:
            current_sum += int(item)
            nums_sum.append(current_sum)
        return nums_sum