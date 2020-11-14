# To return an array that runs through each element calculating sum as each element of new array
# https://leetcode.com/problems/running-sum-of-1d-array/

def runningSum(nums) :
    nums_sum = []
    current_sum = 0
    for item in nums:
        current_sum += int(item)
        nums_sum.append(current_sum)
    return print(nums_sum)

nums = [1,2,3,4,5]
runningSum(nums)