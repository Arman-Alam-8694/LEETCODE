class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def valid(a,b):
            if a<0 or b<0 or a>=row or b>=col or grid[a][b]==0:
                return False
            return True

        def dfs(grid,i,j):
            sm=0
            grid[i][j]=0
            for a,b in [[0,1],[0,-1],[1,0],[-1,0]]:
                if valid(i+a,j+b):
                    sm+=dfs(grid,i+a,j+b)
            return sm+1
        

        row=len(grid)
        col=len(grid[0])
        answer=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 :
            
                    answer=max(answer,dfs(grid,i,j))
        return answer
        
        