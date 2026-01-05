class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        bigN=float("-inf")
        neg=0
        negsum=0
        possum=0
    
        n=len(matrix)
        zero=0
        for i in range(n):
            for j in range(n):
                if matrix[i][j]<0:
                    neg+=1
                    negsum+=matrix[i][j]
                    bigN=max(bigN,matrix[i][j])
                

                elif matrix[i][j]==0:
                    zero+=1
                else:
                    bigN=max(bigN,-matrix[i][j])
                
                    possum+=matrix[i][j]
               

        total=possum+((negsum)*(-1))
    
        if neg%2==0:
            return total
        elif zero>=(neg%2):
            return total
        else:
        
            return total+bigN+bigN

        