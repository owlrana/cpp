# https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(nums: list[int]) -> int:
        pointer = 0
        length = len(nums)
        leftSum = 0
        rightSum = 0
        while pointer < length:
            for i in range(pointer):
                leftSum += nums[i]
                print(nums[i], end = ',')
            print()
            for j in range(pointer+1, length):
                rightSum += nums[j]
                print(nums[j], end = ',')
            print()
            if leftSum == rightSum:
                return pointer
            else:
                print("sum is = ", leftSum, rightSum)
                pointer += 1
                leftSum = 0
                rightSum = 0
        return -1

print(Solution.pivotIndex([-1,-1,-1,1,1,1]))

# WAS NOT ACCEPTED!
# TOOK TOO MUCH TIME!