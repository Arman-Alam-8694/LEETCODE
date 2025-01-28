class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # 8 6
        # 2 6
        row=len(grid)
        col=len(grid[0])
        dist=[]
        maxx=0
        dir=[(0,1),(0,-1),(1,0),(-1,0)]
        def bfs(stack,visited):
            temp=0
            while stack:
                i,j=stack.popleft()
                visited.add((i,j))
                temp+=grid[i][j]
                for x,y in dir:
                    a=x+i
                    b=y+j
                    if 0<=a<row and 0<=b<col and grid[a][b]!=0 and (a,b) not in visited:
                        visited.add((a,b))
                        stack.append((a,b))


            return temp

        visited=set()          
        for i in range(row):
            for j in range(col):

                if grid[i][j]!=0:
                    stack=deque([(i,j)])
                    visited.add((i,j))
                    maxx=max(maxx,bfs(stack,visited))
                    visited=set()

        return maxx

        