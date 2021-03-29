# https://leetcode.com/problems/path-crossing/

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        xy_set = set()
        xy_set.add((0,0))
        xy_set.add((0))
        prev_length = 0
        for char in path:
            if char == "E":
                x += 1
            elif char == "W":
                x -= 1
            elif char == "N":
                y += 1
            else:
                y -= 1
            xy_set.add((x,y))
            if len(xy_set) == prev_length:
                return True
            else:
                prev_length = len(xy_set)
        
        print(xy_set)
        
        return False