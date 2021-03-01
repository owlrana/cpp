# https://leetcode.com/problems/increasing-decreasing-string/submissions/

def sortString(s):
    result = ''
    counter = {}
    for char in s:
        counter[char] = counter.get(char, 0) + 1
    while True:
        for key in sorted (counter.keys()):
            if counter[key] > 0:
                result += key
                counter[key] -= 1
        for key in sorted (counter.keys(), reverse = True):
            if counter[key] > 0:
                result += key
                counter[key] -= 1
        if len(result) >= len(s):
            return result

s = "aaaabbbbcccc"
print(sortString(s))

# 52ms; faster than 96%
# 13.9MB; less than 98%