# Kids with the Greatest No. of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

# Need to define in this way for solution to be accepted
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        l=len(candies)
        maximum = max(candies)
        ans=[]
        
        # This loop iterating through indices takes lesser time 
        for i in range(l):
            if candies[i]+extraCandies >= maximum:
                ans.append(True)
            else:
                ans.append(False)
        return ans

# Faster than 72%
# Memory Less than 82%
# HAVING NO WHITE SPACES, EXTRA LINES, COMMENTS in the final solution helps
# in saving the time so make sure you remove all spaces, lines before
# submitting the code, will help in efficiency -- not noticing in practical
# but still, try removing [the speed is varying 22 ms to 36 ms in same program]