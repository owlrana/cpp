# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution:
    def oddCells(n: int, m: int, indices):
        # Create matrix of size MxN 
        matrix = [[0]*m]*n
        print(matrix)

Solution.oddCells(2, 3, [[0,1], [1,1]])