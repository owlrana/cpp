# https://leetcode.com/problems/reformat-the-string/

class Solution:        
    def reformat(self, s: str) -> str:
        n = len(s)
        numbers = []
        characters = []
        # to insert all chars
        for i in range(n):
            try:
                num = int(s[i])
                numbers.append(str(num))
            except:
                characters.append(s[i])
        if len(numbers) < len(characters)-1 or len(characters) < len(numbers)-1:
            return ""
        start = 0
        if len(numbers) < len(characters):
            start = 1
        for i in range(len(numbers)):
            characters.insert(i*2 - start, numbers[i])
        chars = "".join(char for char in characters)
        return chars
        
s = "a0"
print(Solution.reformat(s))