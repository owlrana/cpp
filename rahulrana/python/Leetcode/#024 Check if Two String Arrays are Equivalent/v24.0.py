# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

def arrayStringsAreEqual(word1, word2):
    string1 = ''
    string2 = ''
    # list of words give, that needs to be added together
    for word in word1:
        string1 += word
    for word in word2:
        string2 += word
    # Finally checking what we have compiled in both strings
    if string1 != string2:
        return False
    return True

word1 = ["ab", 'c', "de"]
word2 = ["a", "bcde"]
print(arrayStringsAreEqual(word1, word2))