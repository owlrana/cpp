# https://leetcode.com/problems/consecutive-characters/

def maxPower(s):
    index1 = 0
    index2 = 1
    appended = []
    length = 1
    while index2 < len(s):
        if s[index1] == s[index2]:
            length += 1
            index2 += 1
            appended.append(length)
        else:
            index1 = index2
            index2 += 1
            length = 1
    try:
        return max(appended)
    except:
        return 1

s = "tourist"
print(maxPower(s))

# 36ms; faster than 89%
# 14.1MB; less than 39%