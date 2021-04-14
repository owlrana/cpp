# https://leetcode.com/problems/plus-one/submissions/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = True
        i = len(digits) - 1
        while add:
            if len(digits) == 1 and digits[0] == 9:
                digits[i] = 0
                digits.insert(0, 1)
                add = False
            elif i == 0 and digits[i] == 9:
                digits[i] = 0
                digits.insert(0, 1)
                add = False
            elif digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                add = False
        return digits