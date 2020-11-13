# Kids with the Greatest No. of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maximum = int(max(candies))
        high_candy_state = []

        # This loop that is special for python takes more time
        # This is solved in version 1.2
        # Loops iterating through indices takes lesser time
        for items in candies:
            if int(items) + extraCandies < maximum:
                high_candy_state.append(False)
            else:
                high_candy_state.append(True)

        return high_candy_state

# Faster than 40% 
# Memory less than 32%