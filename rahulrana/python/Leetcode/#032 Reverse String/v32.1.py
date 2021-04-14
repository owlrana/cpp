# https://leetcode.com/problems/reverse-string/

def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1

s = 'hello'
print(reverseString(s))

# 200 ms; faster than 43%
# 18.7MB; lesser than 16%