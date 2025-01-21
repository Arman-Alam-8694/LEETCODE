from collections import deque
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        #BFS + DFS 


    #     self.grid = grid
    #     self.row, self.col = len(grid), len(grid[0])
    #     self._dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Direction vectors
    #     self.min_cost = [[float('inf')] * self.col for _ in range(self.row)]
    #     self.queue = deque([(0, 0)])
        
    #     # Start the DFS traversal from (0, 0)
    #     self.dfs(0, 0, 0)
        
    #     cost = 0
    #     while self.queue:
    #         cost += 1
    #         size = len(self.queue)
    #         for _ in range(size):
    #             x, y = self.queue.popleft()
    #             for dx, dy in self._dirs:
    #                 self.dfs(x + dx, y + dy, cost)
        
    #     return self.min_cost[self.row - 1][self.col - 1]

    # def dfs(self, i: int, j: int, cost: int) -> None:
    #     while self.is_unvisited(i, j):
    #         self.min_cost[i][j] = cost
    #         self.queue.append((i, j))
    #         direction = self.grid[i][j] - 1  # Get the grid direction
    #         dx, dy = self._dirs[direction]
    #         i += dx
    #         j += dy

    # def is_unvisited(self, i: int, j: int) -> bool:
    #     return 0 <= i < self.row and 0 <= j < self.col and self.min_cost[i][j] == float('inf')

    #0-1 BFS
        row = len(grid)
        col = len(grid[0])
        directions = [(0, 1, 1), (0, -1, 2), (1, 0, 3), (-1, 0, 4)]
        dist = [[float('inf')] * col for _ in range(row)]
        dist[0][0] = 0
        deque_stack = deque([(0, 0, 0)])  # (current cost, row, col)

        while deque_stack:
            ccost, i, j = deque_stack.popleft()
            
            # If this cost is outdated, skip
            if ccost > dist[i][j]:
                continue
            
            for x, y, correct in directions:
                a, b = i + x, j + y
                if 0 <= a < row and 0 <= b < col:
                    # Calculate the new cost
                    ncost = ccost if grid[i][j] == correct else ccost + 1
                    
                    # If this path improves the cost to (a, b), update and enqueue
                    if ncost < dist[a][b]:
                        dist[a][b] = ncost
                        if grid[i][j] == correct:
                            deque_stack.appendleft((ncost, a, b))  # Priority for 0-cost moves
                        else:
                            deque_stack.append((ncost, a, b))  # Low-priority for costly moves

        return dist[row - 1][col - 1]