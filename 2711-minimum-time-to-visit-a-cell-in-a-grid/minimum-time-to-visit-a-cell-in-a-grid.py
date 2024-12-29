class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        if grid[0][1]>1 and grid[1][0]>1:
            return -1
        ways=[(grid[0][0],0,0)]
        visited=set()
        while ways:
            cur_time,i,j=heappop(ways)
            if (i,j) in visited:
                continue
            if i==row-1 and j==col-1:
                return cur_time
            visited.add((i,j))
            for u,v in [(0,1),(0,-1),(1,0),(-1,0)]:
                r=i+u
                c=j+v
                if 0<=r<row and 0<=c<col and ((r,c) not in visited):
                    wait=1 if ((grid[r][c]-cur_time)%2==0) else 0
                    heappush(ways,(max(wait+grid[r][c],cur_time+1),r,c))
        



        