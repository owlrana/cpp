# https://leetcode.com/problems/split-a-string-in-balanced-strings/

def balancedStringSplit(s):
    count = 0
    pair = 0
    for i in s:
        if i == 'R':
            count += 1
        else:
            count -= 1
        if count == 0:
            pair += 1
    return pair

s = "RLRRRLLRLL"
print(balancedStringSplit(s))

# 20 ms; faster than 98%
# 14.1 MB; less than 68%