class Solution(object):
    def spiralOrder(self, matrix):
        h = len(matrix)
        w = len(matrix[0])
        top = 0
        bottom = h-1
        left = 0
        right = w-1
        spiral = []
        while left<=bottom and left<=right:
            for c in range(left,right+1):
                spiral.append(matrix[top][c])
            top+=1  
            for r in range(top,bottom+1):
                spiral.append(matrix[r][right])
            right-=1
            if top<=bottom:
                for c in range(right,left-1,-1):
                    spiral.append(matrix[bottom][c])
                bottom-=1
            
            if left<=right:
                for r in range(bottom,top-1,-1):
                    spiral.append(matrix[r][left])
                left+=1
        return spiral
