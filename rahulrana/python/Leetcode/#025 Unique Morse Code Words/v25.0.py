# https://leetcode.com/problems/unique-morse-code-words/
from collections import Counter

morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....",
                "..",".---","-.-",".-..","--","-.","---",".--.",
                "--.-",".-.","...","-","..-","...-",".--","-..-",
                "-.--","--.."]

# lowercase letters are morse code's list [ord - 97] 
def uniqueMorseRepresentations(words):
    morse_list = []
    for word in words:
        morse_word = ""
        for chars in word:
            morse_word += morse_codes[ord(chars) - 97]
        morse_list.append(morse_word)
    return len(Counter(morse_list).keys())    

words = ["gin", "zen", "gig", "msg"]
print(uniqueMorseRepresentations(words))

# 32 ms; faster than 82%
# 14.2 MB; less than 76%