# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

def subtractProductAndSum(n):
    sums = 0
    multiply = 1
    while n != 0:
        multiply *= int(n%10)
        sums += int(n%10)
        n = int(n/10)
    return multiply - sums

n = 4421
print(subtractProductAndSum(n))

# 20 ms; faster than 98%
# 13.9 MB; less than 86%