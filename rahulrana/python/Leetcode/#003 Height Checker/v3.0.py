# Non-Decreasing way to stand students
# https://leetcode.com/problems/height-checker/

# sort the array and compare with the original one to see how many items need to be moved

def heightChecker(heights):
    
    heights_sorted = sorted(heights)
    items_misplaced = 0
    for i in range(0, len(heights)):
        if heights[i] != heights_sorted[i]:
            print("Should have been: ", heights[i])
            print("And there is: ", heights_sorted[i])
            items_misplaced += 1
    return print(items_misplaced)

heights = [1,1,4,2,1,3]
heightChecker(heights)