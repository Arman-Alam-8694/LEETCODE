# class Solution:
#     def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
#         def calculate(k,last,queue):
#             directions=[(0,1),(1,0),(-1,0),(0,-1)]
#             m=len(grid)
#             n=len(grid[0])
#             prev=0
#             invalid=deque([])
#             while queue:    
#                 x,y=queue.popleft()
#                 if grid[x][y]<k and grid[x][y]!=-1 :
#                     # if k==6:
#                         # print(grid[x][y])
#                     grid[x][y]=-1
#                     last+=1
#                     for dx,dy in directions:
#                         if 0<=dx+x<m and 0<=dy+y<n and grid[dx+x][dy+y]!=-1:
#                             queue.append((dx+x,dy+y))
#                 else:
#                     if grid[x][y]!=-1:
#                         invalid.append((x,y))

#             return last,invalid
            
                    

#         original=queries[:]
#         queries.sort()
#         queue=deque()
#         queue.append((0,0))
#         last_point=0
#         prev=-1
#         mapp=defaultdict(int)
#         for i in queries:
#             if i in mapp:
#                 continue
#             ans,queue=calculate(i,last_point,queue)
#             last_point=ans
#             mapp[i]=last_point
        
#         res=[]
#         for i in original:
#             res.append(mapp[i])


#         return res

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
