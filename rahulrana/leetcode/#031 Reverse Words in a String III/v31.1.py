# https://leetcode.com/problems/reverse-words-in-a-string-iii/ 

def reverseWords(s):
    rev = ''
    words_list = s.split()
    for word in words_list:
        rev += word[::-1]
        rev += ' '
    return rev[:len(rev)-1]

s = "Let's take LeetCode contest"
print(reverseWords(s))

# 24ms; faster than 97%
# 14.8MB; less than 60%