# Number of good pairs
# https://leetcode.com/problems/number-of-good-pairs/

# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.

def numIdenticalPairs(nums):
    pair = 0
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            if nums[i] == nums[j]:
                if j > i:
                    pair += 1
    return pair

nums = [1,2,3]
print(numIdenticalPairs(nums))

# 28 ms; faster than 88%
# 13.9 MB; less than 83%