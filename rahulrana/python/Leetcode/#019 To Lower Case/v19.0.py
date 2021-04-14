# https://leetcode.com/problems/to-lower-case/

def toLowerCase(str):
    lowchar = ''
    for char in str:
        if ord(char) <= 90 and ord(char) >= 60:
            lowchar += chr(ord(char) + 32)
        else:
            lowchar += char
    return lowchar

s = '&ightinG is NOT oK'
print(toLowerCase(s))

# 24 ms; faster than 87%
# 14.1 MB; less than 24%