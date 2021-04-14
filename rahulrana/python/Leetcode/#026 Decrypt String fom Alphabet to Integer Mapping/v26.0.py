# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

def freqAlphabets(s):
    word = ''
    i = 0
    while i < len(s):
        try:
            if s[i+2] == '#':
                character = chr(96 + int(s[i] + s[i+1]))
                i += 3
            else:
                character = chr(96 + int(s[i]))
                i += 1
        except:
            character = chr(96 + int(s[i]))
            i += 1
        word += character
    return word

s = "1326#"
print(freqAlphabets(s))

# 28ms; faster than 80%
# 14.3MB; less than 5%