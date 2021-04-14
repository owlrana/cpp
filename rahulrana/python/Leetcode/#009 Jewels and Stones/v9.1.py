# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/

def numJewelsInStones(J, S):
    count = 0
    for char in S:
        if char in J:
            count += 1
    return count

J = "aA"
S = "aAAbbbb"
print(numJewelsInStones(J, S))

# 28 ms; faster than 78%
# 14 MB; less than 26%