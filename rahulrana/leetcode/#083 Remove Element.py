# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        i = 0
        cycle = 0
        while cycle < length:
            if nums[i] == val:
                del nums[i]
                cycle += 1
            else:
                cycle += 1
                i += 1
        return len(nums)