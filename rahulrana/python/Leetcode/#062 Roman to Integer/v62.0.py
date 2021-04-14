# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(s):
        romans = {  "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000}
        print(romans, type(romans))
        previous = 0
        sum = 0
        length = len(s)
        for i in reversed(range(length)):
            if romans[s[i]] >= previous:
                sum += romans[s[i]]
                previous = romans[s[i]]
            else:
                sum -= romans[s[i]]
                previous = romans[s[i]]
        print(sum)
        return sum

assert Solution.romanToInt("MCMXCIV") == 1994