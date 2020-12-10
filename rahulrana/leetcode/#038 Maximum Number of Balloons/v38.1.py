# https://leetcode.com/problems/maximum-number-of-balloons/submissions/

def maxNumberOfBalloons(text):
    # initiating a key for each word in dictionary using loop
    fTable = {char: 0 for char in 'balon'}
    # associate the value with count
    for char in text:
        if char in fTable:
            fTable[char] += 1
    # now divide by 2 to know how many words formed
    fTable['l'] = fTable['l']/2
    fTable['o'] = fTable['o']/2
    return min(fTable.values())

text = "slaolnblo"
print(maxNumberOfBalloons(text))

# 28ms; faster than 89%
# 14.4MB; less than 22%