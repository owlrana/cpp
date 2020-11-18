# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

def maxDepth(s):
    counts = 0
    max = 0
    for char in s:
        if char == '(':
            counts += 1
        elif char == ')':
            counts -= 1
        if counts > max:
            max = counts
    return max

s = "1+(2*3)/(2-1)"
print(maxDepth(s))

# 28 ms; faster than 82%
# 14.1 MB; less than 33%