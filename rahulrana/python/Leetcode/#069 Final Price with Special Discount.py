# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/submissions/

class Solution:
    def finalPrices(prices):
        n = len(prices)
        finalPrice = []
        for i in range(n):
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    finalPrice.append(prices[i] - prices[j])
                    break
                if j == n-1:
                    finalPrice.append(prices[i])
        finalPrice.append(prices[n-1])
        return finalPrice
assert Solution.finalPrices([8,4,6,2,3]) == [4,2,4,2,3]