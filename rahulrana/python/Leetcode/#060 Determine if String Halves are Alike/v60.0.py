# https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(s: str) -> bool:
        mid = len(s)//2
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        one, two = 0, 0
        print()
        print("Loop starting. i is =", s[0], "mid is ", s[mid])
        print()
        for i in range(mid):
            print("Inside loop. Values are =", s[i], "mid is ", s[i+mid])
            if s[i] in vowels:
                print("Found in 1st String= ", s[i])
                one += 1
            if s[i+mid] in vowels:
                print("Found in 2nd String= ", s[i+mid])
                two += 1
        if one == two:
            return True
        return False

assert (Solution.halvesAreAlike("baaiik")) == True