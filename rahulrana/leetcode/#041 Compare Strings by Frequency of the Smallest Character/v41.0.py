# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

def f(word):
    minimum = 130 # anything greater than normal english lowercases
    for char in word:
        if ord(char) < minimum:
            minimum = ord(char)
    frequency = 0
    for i in range(len(word)):
        if word[i] == chr(minimum):
            frequency += 1
    return frequency

def numSmallerByFrequency(queries, words):
    output_list = []
    for word1 in queries:
        lessthan = 0
        for word2 in words:
            if f(word1) < f(word2):
                lessthan += 1
        output_list.append(lessthan)
    return output_list

queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]
print(numSmallerByFrequency(queries, words))

# TIME LIMIT EXCEEDED