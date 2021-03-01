# https://leetcode.com/problems/increasing-decreasing-string/

def sortString(s: str) -> str:
    result = ''
    counter = {}
    for char in s:
        counter[char] = counter.get(char, 0) + 1
    # will be run for no. of unique chrs
    while len(result) != len(s):
        # alphabetical append
        for key in sorted (counter.keys()):
            if counter[key] > 0:
                result += key
                counter[key] -= 1
        # reverse append
        for key in sorted (counter.keys(), reverse = True):
            if counter[key] > 0:
                result += key
                counter[key] -= 1
    return result
s = "aaaabbbbcccc"
print(sortString(s))

# 52ms; faster than 96%
# 14.3MB; less than 12%