# https://leetcode.com/problems/increasing-decreasing-string/

def sortString(s: str) -> str:
    result = ''
    counter = {}
    for char in s:
        counter[char] = counter.get(char, 0) + 1
    

    return result