# https://leetcode.com/problems/maximum-number-of-balloons/

def maxNumberOfBalloons(text):
    ctext_list = []
    for char in text:
        ctext_list.append(char)
    balloon = 'balloon'
    index = 0
    words = 0
    while ctext_list:
        if balloon[index] in ctext_list:
            ctext_list.remove(balloon[index])
            index += 1
        else:
            return words
        if index == len(balloon):
            index = 0
            words += 1
    return words

text = "leetcode"
print(maxNumberOfBalloons(text))

# 528ms; faster than 5%
# 14.5MB; less than 6%