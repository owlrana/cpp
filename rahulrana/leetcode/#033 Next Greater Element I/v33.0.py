# https://leetcode.com/problems/next-greater-element-i/

# git check

def nextGreaterElement(nums1, nums2):
    nextGE = []
    for i in range(len(nums1)):
        print('this loop for', nums1[i])
        if max(nums2) <= nums1[i]:
            print(max(nums2), 'is less than or equal to ', nums1[i])
            nextGE.append(-1)
            print("Exit IF")
        else:
            print("entered else")
            mini = max(nums2)
            for j in range(i-1, len(nums2)):
                print("entered for")
                if nums2[j] < mini and nums2[j] > nums1[i]and j > i:
                    print("entered if")
                    nextGE.append(nums2[j])
                    break
                if len(nums2) == i:
                    break
            if nums1[i] < mini:
                nextGE.append(mini)
            else:
                nextGE.append(-1)
    return nextGE

nums1 = [4,1,2] 
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))

# output -1, 3, -1