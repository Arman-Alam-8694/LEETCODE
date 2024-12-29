class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]
        q = deque([(0,0,0)])
        visited[0][0] = True
        dire = [(1,0),(0,1),(-1,0),(0,-1)]
        while(q):
            i,j,obst = q.popleft()
            if(i == m-1 and j == n-1):
                return obst
            for dx,dy in dire:
                x,y = i+dx,j+dy
                if(0<=x<m and 0<=y<n and not visited[x][y]):
                    visited[x][y] = True
                    if(grid[x][y]):
                        q.append((x,y,obst+1))
                    else:
                        q.appendleft((x,y,obst))
        return -1
            
            
        