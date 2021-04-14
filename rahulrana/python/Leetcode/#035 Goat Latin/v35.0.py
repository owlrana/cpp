# https://leetcode.com/problems/goat-latin/

def toGoatLatin(S):
    words_list = S.split()
    counter = 0
    gword_list = []
    for word in words_list:
        if word[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            word += 'ma'
        else:
            word = list(word)
            cons = word.pop(0)
            word.append(cons)
            word.append('ma')
            word = "".join(word)
        a = ''
        for i in range(counter + 1):
            a += 'a'
        counter += 1
        word += a
        gword_list.append(word)
    return " ".join(gword_list)

S = "Each word consists of lowercase and uppercase letters only"
s = toGoatLatin(S)
if S == S:
    print('ok')

# 28ms; faster than 78%
# 14.3MB; less than 15%