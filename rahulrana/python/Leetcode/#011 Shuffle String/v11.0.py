# Shuffle String
# https://leetcode.com/problems/shuffle-string/submissions/

def restoreString(s, indices):
    new_string = ""
    for i in range(len(s)):
        for j in range(len(s)):
            if i == indices[j]:
                new_string += s[j]
    return new_string

s = "aiohn"
indices = [3,1,4,2,0]

print(restoreString(s, indices))

# 112 ms; faster than 5%
# 14 MB; better than 85%