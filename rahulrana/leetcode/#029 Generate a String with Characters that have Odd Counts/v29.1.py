# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

def generateTheString(n: int) -> str:
    if (n%2) != 0:
        return 'a' * n
    else:
        return ('a' * (n-1)) + 'b'

# 20 ms; faster than 98%
# 14 MB; less than 50%