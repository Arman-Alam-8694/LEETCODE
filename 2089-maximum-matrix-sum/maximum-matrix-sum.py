class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        bigN=float("inf")
        neg=0
        possum=0
    
        n=len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j]<0:
                    neg+=1

             
                bigN=min(bigN,abs(matrix[i][j]))
                
                possum+=abs(matrix[i][j])
               

    
        if neg%2==0:
            return possum
        else:
        
            return possum+(-bigN)+(-bigN)

        