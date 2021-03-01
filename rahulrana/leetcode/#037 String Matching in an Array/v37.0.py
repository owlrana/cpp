# https://leetcode.com/problems/string-matching-in-an-array/

def stringMatching(words):
    substring_list = []
    for word1 in words:
        for word2 in words:
            if word1 in word2 and word1 != word2 and word1 not in substring_list:
                substring_list.append(word1)
    return substring_list

words = ["leetcode","et","code"]
print(stringMatching(words))

# 24ms; faster than 99%
# 14.3MB; less than 25%