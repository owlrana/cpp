class Solution:
    def shuffle(self, nums, mid):
        numout = []
        for i in range (0, mid):
            numout.append(nums[i])
            numout.append(nums[i + mid])
        return numout