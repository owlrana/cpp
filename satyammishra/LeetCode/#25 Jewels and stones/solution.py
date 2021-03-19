class Solution:
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for character in stones:
            if character in jewels:
                count += 1
               # stones = stones.replace(character, '', 1)
             
        print(count)

obj = Solution()
a = "z"
b = "aAAbcdzz"
obj.numJewelsInStones(a,b)



        