from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
    
        # Edge case: start or end cell is blocked
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        
        # Priority queue for BFS: (path_length, x, y)
        pq = deque([(0, 0, 0)])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        dist = [[float('inf')] * n for _ in range(n)]
        while pq:
            plength,i,j=pq.popleft()
            plength+=1
            if i==n-1 and j==n-1:
                return plength
            for x,y in directions:
                a=x+i
                b=y+j
                if 0<=a<n and 0<=b<n  and grid[a][b]!=1:
                    if plength<dist[a][b]:
                        pq.append((plength,a,b))
                        dist[a][b]=plength
        return -1

            