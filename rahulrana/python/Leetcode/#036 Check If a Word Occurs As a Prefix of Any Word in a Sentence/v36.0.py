# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

def isPrefixOfWord(sentence: str, searchWord: str):
    words_list = sentence.split()
    indexed = 0
    for word in words_list:
        if word.startswith(searchWord):
            return indexed + 1
        indexed += 1
    return -1

sentence = "i love eating burger"
searchWord = "burg"
print(isPrefixOfWord(sentence, searchWord))

# 28ms; faster than 68%
# 14.2MB; less than 15%