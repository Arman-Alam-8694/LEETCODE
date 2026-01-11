class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row=len(matrix)
        col=len(matrix[0])
        prefix=[[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j]=="0":
                    prefix[i][j]=0
                elif i!=0:
                    prefix[i][j]=prefix[i-1][j]+1
                else:
                    prefix[i][j]=1

        ans=0
        for i in range(row):
            stack=[]
            for j in range(col):
                left=j
                while stack and prefix[i][j]<stack[-1][0]:
                    val,left=stack.pop()
                    ans=max(ans,val*(j-left))
                
                    
               

                if prefix[i][j]>0:
                    stack.append((prefix[i][j],left))
            while stack:
                val,left=stack.pop()
                ans=max(ans,val*(col-left))
        return ans
                

        