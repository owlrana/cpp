class Solution:
    def heightChecker(self, heights):
        heights_sorted = sorted(heights)
        items_misplaced = 0
        for i in range(0, len(heights)):
            if heights[i] != heights_sorted[i]:
                items_misplaced += 1
        return items_misplaced

# Time 28 ms; faster than 94%
# Memory 14.1MB; less than 26%