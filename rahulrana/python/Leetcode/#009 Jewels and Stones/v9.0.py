# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/

def numJewelsInStones(J, S):
    jewels = []
    count = 0
    for char in J:
        jewels.append(char)
    for char in S:
        if char in jewels:
            count += 1
    return count

J = "aA"
S = "aAAbbbb"
print(numJewelsInStones(J, S))

# 32 ms; faster than 50%
# 14 MB; less than 26%