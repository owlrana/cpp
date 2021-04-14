# https://leetcode.com/problems/plus-one/submissions/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        n = len(digits)
        rev = []
        add = True
        for i in reversed(range(n)):
            if i == 0 and digits[i] == 9 and add:
                rev.append(0)
                rev.insert(0,1)
            elif digits[i] == 9 and add:
                rev.insert(0,0)
            elif add:
                rev.insert(0, digits[i]+1)
                add = False
            else:
                rev.insert(0, digits[i])
        return rev