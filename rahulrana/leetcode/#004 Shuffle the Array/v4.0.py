# Shuffle the Array
# https://leetcode.com/problems/shuffle-the-array/

# Given array and the no. of elements to be broken into as a group

def shuffle(nums, mid):
    numout = []
    for i in range (0, mid):
        numout.append(nums[i])
        numout.append(nums[i + mid])
    return print(numout)

nums = [1,1,2,2]
mid = 2
shuffle(nums, mid)