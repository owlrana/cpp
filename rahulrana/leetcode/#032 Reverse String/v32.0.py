# https://leetcode.com/problems/reverse-string/

def reverseString(s):
    s = list(s)
    length = len(s)
    for i in range(int(length/2)):
        char = s[i]
        s[i] = s[length -i -1]
        s[length -i -1] = char
    return s

s = 'hello'
print(reverseString(s))

# 204 ms; faster than 26%
# 18.8MB; lesser than 11%