class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dir=[(0,1),(1,0)]
        def is_valid(x,y):
            if 0<=x<m and 0<=y<n and obstacleGrid[x][y]!=1:
                return True
            return False
        memo={}
        def recur(i,j):
            if i==m-1 and j==n-1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            ways=0
            for u,v in dir:
                x=i+u
                y=j+v
                if is_valid(x,y):
                    ways+=recur(x,y)
            memo[(i,j)]=ways
            return memo[(i,j)]
        
        return recur(0,0)
        