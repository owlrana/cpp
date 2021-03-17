# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(grid):
        m = len(grid)
        n = len(grid[0])
        count = 0
        end = -1
        for i in range(m-1, -1, -1):
            for j in range(n-1, end, -1):
                if grid[i][j] < 0:
                    count +=1
                else:
                    end += 1
        return count

assert Solution.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]) == 8