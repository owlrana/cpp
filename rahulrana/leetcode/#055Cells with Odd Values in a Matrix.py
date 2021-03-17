# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution:
    def oddCells(n: int, m: int, indices):
        # Create matrix of size MxN 
        matrix = []
        for i in range(n):
            lst = []
            for j in range(m):
                lst.append(0)
            matrix.append(lst)

        print(matrix)

        for index in indices:
            row = index[0]
            col = index[1]
            for i in range(n):
                matrix[i][col] += 1
            for i in range(m):
                matrix[row][i] += 1
        print(matrix)
        count = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] % 2 != 0:
                    count += 1
        return count 

print(Solution.oddCells(2, 3, [[0,1], [1,1]]))