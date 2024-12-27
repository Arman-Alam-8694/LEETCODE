from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        row=len(grid)
        col=len(grid[0])
        rotted=0
        empty=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    rotted+=1
                    grid[r][c]==-1
                    queue.append((r,c))
                elif grid[r][c]==0:
                    empty+=1
        if empty==row*col:
            return 0
        
        
        
        
        minute=0
        def isvalid(a,b):
            return 0<=a<row and 0<=b<col

        dir=[(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            n=len(queue)
            for _ in range(n):
                i,j=queue.popleft()
                for u,v in dir:
                    nex=i+u
                    ney=j+v
                    if isvalid(nex,ney):
                        if grid[nex][ney]==1:

                            rotted+=1
                            grid[nex][ney]=-1
                            queue.append((nex,ney))
            if queue:
                minute+=1
      

        return minute if rotted+empty==row*col else -1
