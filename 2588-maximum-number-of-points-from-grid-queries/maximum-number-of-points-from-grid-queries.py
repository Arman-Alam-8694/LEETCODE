from heapq import heappop, heappush
from collections import defaultdict
from typing import List
from collections import deque

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        # Min-Heap to always expand the smallest value first
        min_heap = [(grid[0][0], 0, 0)]  # (value, row, col)
        grid[0][0] = -1  # Mark as visited
        visited_count = 0
        
        # Sort queries and map results
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        query_map = {}
        
        for idx, threshold in sorted_queries:
            # Expand all reachable cells with value < threshold
            while min_heap and min_heap[0][0] < threshold:
                val, x, y = heappop(min_heap)
                visited_count += 1
                
                # Explore neighbors
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                        heappush(min_heap, (grid[nx][ny], nx, ny))
                        grid[nx][ny] = -1  # Mark as visited
            
            # Store the result for this query
            query_map[idx] = visited_count
        
        # Build the final result based on original query order
        return [query_map[i] for i in range(len(queries))]
