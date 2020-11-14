def runningSum(num_list: List[num]):
    nums_sum = []
    current_sum = 0
    for item in nums:
        current_sum += int(item)
        nums_sum.append(current_sum)
    return print(nums_sum)

nums = [1,2,3,4,5]