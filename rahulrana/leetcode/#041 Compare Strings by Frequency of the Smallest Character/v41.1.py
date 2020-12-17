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
    q_fr = []
    w_fr = []
    for w1 in queries:
        q_fr.append(f(w1))
    for w2 in words:
        w_fr.append(f(w2))
    for i in q_fr:
        lessthan = 0
        for j in w_fr:
            if i < j:
                lessthan += 1
        output_list.append(lessthan)
    return output_list

queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]
print(numSmallerByFrequency(queries, words))

# 582ms; faster than 48%
# 14.7MB; less than 22%