# https://leetcode.com/problems/sum-of-unique-elements/submissions/

# using " dict.get(n, 0) +1 "to initiate value of dict[n] by 0 or inc by 1 

class Solution:
    def sumOfUnique(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        sum = 0
        for key in freq.items():
            if freq[key] == 1:
                sum += int(key)
        return sum

#urls[url] = urls.get(url, 0) + 1
