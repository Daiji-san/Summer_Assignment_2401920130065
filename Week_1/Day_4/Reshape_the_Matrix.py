class Solution(object):
    def matrixReshape(self, mat, r, c):
        h = len(mat)
        w = len(mat[0])
        if h*w != r*c:
            return mat
        res = []
        row_build = []
        for i in range(h):
            for j in range(w):
                element=mat[i][j]
                row_build.append(element)
                if len(row_build)==c:
                    res.append(row_build)
                    row_build=[]
        return res
