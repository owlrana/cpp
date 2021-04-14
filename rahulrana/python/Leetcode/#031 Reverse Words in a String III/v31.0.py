# https://leetcode.com/problems/reverse-words-in-a-string-iii/ 

def reverseWords(s):
    rev = ''
    for i in range (len(s)):
        if s[i] == ' ' or i == (len(s)-1):
            j = i - 1
            if i == len(s) - 1:
                j = i
            while s[j] != ' ' and j >= 0:
                rev += s[j]
                j -= 1
            if len(s) != len(rev):
                rev += ' '
    return rev

s = "Let's take LeetCode contest"
print(reverseWords(s))

# 128ms; faster than 6%
# 14.8MB; less than 32%