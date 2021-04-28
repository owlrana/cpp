# Check file

class Solution:
    def sumZero(n: int):
        lst = []
        for i in range(1, n//2 + 1):
            lst.append(i)
            lst.append(i*(-1))
        if len(lst) != n:
            lst.append(0)
        return lst

print(Solution.sumZero(2))