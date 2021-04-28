# https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix):
        out, ins = len(matrix) - 1, len(matrix[0]) - 1
        for i in range(out):
            for j in range(ins):
                if matrix [i][j] != matrix [i+1][j+1]:
                    return False
        return True