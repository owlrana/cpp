# https://leetcode.com/problems/reverse-bits/

# input of the bits is given as int

def reverseBits(n):
    result = 0
    for i in range(32):
        result <<= 1
        print(result)
        result |= n & 1
        print(n)
        n >>= 1
        print(n)
    return result 

n = 43261596
print(reverseBits(n))