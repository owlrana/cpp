# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(nums):
        evenNums = 0
        for number in nums:
            if len(str(number)) % 2 == 0:
                evenNums += 1
        return evenNums
print(Solution.findNumbers([12,345,2,6,7896]))