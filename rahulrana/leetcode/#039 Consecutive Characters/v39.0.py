# https://leetcode.com/problems/consecutive-characters/

def maxPower(s):
    index1 = 0
    index2 = 1
    length = 1
    max_length = 1
    while index2 <= len(s) - 1:
        if s[index1] == s[index2]:
            print(s[index1], '&', s[index2])
            index2 += 1
            length += 1
            print(length)
        else:
            index1 = index2
            index2 += 1
            print(s[index1], 'and', s[index2])
            print(length)
        if length > max_length:
            max_length = length
    return max_length

s = "abbcccddddeeeeedcba"
print(maxPower(s))