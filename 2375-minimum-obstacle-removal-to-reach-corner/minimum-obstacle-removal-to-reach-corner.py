from collections import deque
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        for i in grid:
            print(i)
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        queue=deque([(0,0,0)])
        visited=set()
        prev=0
        def if_valid(x,y):
            if (0<=x<m and 0<=y<n) and ((x,y) not in visited):
                return True
            return False
        while queue:
            i,j,obs=queue.popleft()
            
            if (i, j) == (m - 1, n - 1):  # Reached the bottom-right corner
                    return obs
            for u,v in directions:
                newx=i+u
                newy=j+v
                if if_valid(newx,newy):
                    visited.add((newx,newy))
                    if grid[newx][newy]==0:
                        queue.appendleft((newx,newy,obs))
                    else:
                        queue.append((newx,newy,obs+1))
            
   
                

