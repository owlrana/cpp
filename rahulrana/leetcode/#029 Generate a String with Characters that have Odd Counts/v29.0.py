# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

def generateTheString(n: int) -> str:
    odd_string = ''
    if (n%2) != 0:
        for i in range(n):
            odd_string += 'a'
    else:
        for i in range(n-1):
            odd_string += 'a'
        odd_string += 'b'
    return odd_string
n = 12
print(generateTheString(n))

# 32 ms; faster than 50%
# 14.3 MB; less than 10%