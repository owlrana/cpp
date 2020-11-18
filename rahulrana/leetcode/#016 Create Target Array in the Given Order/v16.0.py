# https://leetcode.com/problems/create-target-array-in-the-given-order/

def createTargetArray(nums, index):
    new_list = []
    for i in range(len(index)):
        new_list.insert(index[i], nums[i])
    return new_list

nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(createTargetArray(nums, index))

# 28 ms; faster 88%
# 13.9 MB; less than 85%