# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

def sumOddLengthSubarrays(arr):     
    sum = 0
    l = len(arr)
    for i in range(l):
        for j in range(i, l, 2):
            for k in range(i, j + 1, 1):
                sum += arr[k]
    return sum

arr = [1,4,2,5,3]
print(sumOddLengthSubarrays(arr))

# 140 ms; faster than 12%
# 14.3 MB; less than 16%