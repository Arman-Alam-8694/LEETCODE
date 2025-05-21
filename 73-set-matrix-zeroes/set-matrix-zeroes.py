class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        trow=False
        tcol=False
        # print(matrix[0][1])
        for i in range(row):
            for j in range(col):
                if i==0 or j==0:
                    if i==0 and matrix[i][j]==0:
                        trow=True
                    if j==0 and matrix[i][j]==0:
                        tcol=True
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        # print(trow,tcol)
        # print(matrix)
        for i in range(1,row):
            if matrix[i][0]==0:
                for k in range(col):
                    matrix[i][k]=0
        
        for i in range(1,col):
            if matrix[0][i]==0:
                for k in range(row):
                    matrix[k][i]=0

        if trow:
            for k in range(col):
                 matrix[0][k]=0
        if tcol:
            for k in range(row):
                    matrix[k][0]=0
        return matrix

                