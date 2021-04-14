# How Many Numbers Are Smaller Than the Current Number
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

def smallerNumbersThanCurrent(nums):
    smaller_nums = []
    for n in nums:
        count = 0
        for m in nums:
            if m < n:
                count += 1
        smaller_nums.append(count)
    return smaller_nums

nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))

# 272 ms; faster than 43%
# 14.1 MB; less than 86%