class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        left=0
        right=len(matrix[0])
        up=0
        down=len(matrix)
        row=set()
        col=set()
        for r in range(down):
            for c in range(right):
                if matrix[r][c]==0:
                    row.add(r)
                    col.add(c)
        for r in row:
            for i in range(0,right):
                matrix[r][i]=0
                
        for c in col:
            for j in range(0,down):
                matrix[j][c]=0