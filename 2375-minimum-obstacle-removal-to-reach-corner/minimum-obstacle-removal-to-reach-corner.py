from heapq import heappop, heappush

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        heap = [(0, 0, 0)]  # (obstacles, x, y)
        visited = set()
        
        while heap:
            obs, i, j = heappop(heap)
            if (i, j) == (m - 1, n - 1):  # Reached the bottom-right corner
                return obs
            if (i, j) in visited:
                continue
            visited.add((i, j))
            
            for dx, dy in directions:
                newx, newy = i + dx, j + dy
                if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in visited:
                    if grid[newx][newy] == 0:
                        heappush(heap, (obs, newx, newy))  # No additional obstacle
                    else:
                        heappush(heap, (obs + 1, newx, newy))  # Remove an obstacle
        
        return -1  # If there's no valid path
