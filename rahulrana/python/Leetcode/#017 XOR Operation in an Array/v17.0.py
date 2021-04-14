# https://leetcode.com/problems/xor-operation-in-an-array/

def xorOperation(n, start):
    nums = []
    result = start
    for i in range(n):
        nums.append(start + (2*i))
    for i in range(n-1):
        result = result ^ nums[i+1]
    return result

n = 5
start = 0
print(xorOperation(n, start))

# 24 ms; faster than 94%
# 14.1 MB; less than 32%