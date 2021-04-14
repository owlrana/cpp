# https://leetcode.com/problems/count-good-triplets/

# Check all triplets in the given array

# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c

# These are the absolute values ^

class Solution:
    def countGoodTriplets(arr, a, b, c):
        length = len(arr)
        count = 0
        for k in range(2, length):
            for j in range(1, k):
                for i in range(j):
                    if (abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b
                            and abs(arr[k] - arr[i]) <= c) :
                        count += 1
        return count

print(Solution.countGoodTriplets([3,0,1,1,9,7], 7,2,3))

# faster than 30%
# lesser than 88%