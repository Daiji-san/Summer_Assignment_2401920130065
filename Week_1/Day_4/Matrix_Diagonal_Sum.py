#Problem Link --> https://leetcode.com/problems/matrix-diagonal-sum/
#Description --> Given a square matrix mat, return the sum of the matrix diagonals.
#                Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are 
#                not part of the primary diagonal.

class Solution(object):
    def diagonalSum(self, mat):
        n = len(mat)
        total_sum = 0

        for i in range(n):
            total_sum += mat[i][i]
            total_sum += mat[i][n - 1 - i]
        
        if n % 2 != 0:
            total_sum -= mat[n // 2][n // 2]
            
        return total_sum
