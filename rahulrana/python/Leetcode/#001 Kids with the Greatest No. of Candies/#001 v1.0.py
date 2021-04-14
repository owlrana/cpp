# Kids with the Greatest No. of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

# candies[i] tells the number of candies ith kid has; 
# length constraints: 2 <= 100 
# list candies

# no. of extra candies to distribute
# int extraCandies

def highest_candy_calc (candies, extraCandies):
    
    if not (len(candies) >= 2 and len(candies) <= 100 ):
        return "INVALID INPUT"
    elif max(candies) > 100 or min(candies) < 1:
        return "INVALID INPUT"
    elif extraCandies < 1 or extraCandies > 50:
        return "INVALID INPUT"

    maximum = int(max(candies))
    high_candy_state = []

    for items in candies:
        if int(items) + extraCandies < maximum:
            high_candy_state.append(False)
        else:
            high_candy_state.append(True)

    return high_candy_state

# Getting input as space separated values to convert into list
candies = [int(item) for item in input("Enter the list items : ").split()] 

extraCandies = int(input("Enter extra candies to be distributed: "))

print(highest_candy_calc(candies, extraCandies))