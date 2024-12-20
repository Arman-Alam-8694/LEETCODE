class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row=len(matrix)
        col=len(matrix[0])
        temp=col-1
        for i in range(row):
            for j in range(i+1,col):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for i in range(col//2):
            for j in range(row):
                matrix[j][temp-i],matrix[j][i]=matrix[j][i],matrix[j][temp-i]
        return matrix
