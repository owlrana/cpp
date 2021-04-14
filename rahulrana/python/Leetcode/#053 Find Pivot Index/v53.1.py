class Solution:
    def pivotIndex(nums: list[int]) -> int:
        length = len(nums)
        leftSum = 0
        rightSum = sum(nums)
        for i in range(length):
            leftSum += nums[i]
            if leftSum == rightSum:
                return i
            rightSum -= nums[i]
        return -1