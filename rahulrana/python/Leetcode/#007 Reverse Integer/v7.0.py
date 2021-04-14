# Reverse the integer number
# https://leetcode.com/problems/reverse-integer/submissions/

def reverse(self, x):
    rev_string = str(x)[::-1]
    rev = ""
    for i in range(len(rev_string)):
        try:
            int(rev_string[i])
            rev += (rev_string[i])
        except:
            if int("-"+rev) <= -2147483647:
                return 0
            return int("-"+rev)
    if int(rev) >= 2147483648:
        return 0
    return int(rev)

# 16ms; faster than 99%
# 14.2MB; less than 6%