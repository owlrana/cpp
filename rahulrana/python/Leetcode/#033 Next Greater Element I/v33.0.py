# https://leetcode.com/problems/next-greater-element-i/

# git check

def nextGreaterElement(nums1, nums2):
    next_greater = []
    for num in nums1:
        start = nums2.index(num)
        for j in range(start, len(nums2)):
            if nums2[j] > num:
                next_greater.append(nums2[j])
                break
        if len(next_greater) < nums1.index(num) + 1:
            next_greater.append(-1)
    return next_greater

nums1 = [4, 1, 2] 
nums2 = [1,2,3,4]
print(nextGreaterElement(nums1, nums2))

# 88ms; faster than 14%
# 14.4MB; less than 78%