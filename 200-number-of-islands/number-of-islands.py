class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid(a,b):
            if a<0 or b<0 or a>=row or b>=col or visited[a][b]==1 or grid[a][b]=="0":
                return False
            return True

        def dfs(grid,visited,i,j):
            visited[i][j]=1
          
            for a,b in [[0,1],[0,-1],[1,0],[-1,0]]:
                if valid(i+a,j+b):
                    dfs(grid,visited,i+a,j+b)
            return 1

        row=len(grid)
        col=len(grid[0])
        visited=[[0]*col for i in range(row)]
        answer=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1" and visited[i][j]==0:
                    answer+=dfs(grid,visited,i,j)
        return answer
        
        