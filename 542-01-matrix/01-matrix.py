from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        result = [[float('inf')] * col for _ in range(row)]
        queue = deque()
        
        # First pass: Find all 0s and add them to queue
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))
        
        # Directions for 4-directional movement
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # BFS from all 0s simultaneously
        while queue:
            curr_i, curr_j = queue.popleft()
            curr_dist = result[curr_i][curr_j]
            
            # Check all 4 directions
            for di, dj in directions:
                new_i, new_j = curr_i + di, curr_j + dj
                
                # Check if the new position is valid and needs updating
                if (0 <= new_i < row and 
                    0 <= new_j < col and 
                    result[new_i][new_j] > curr_dist + 1):
                    result[new_i][new_j] = curr_dist + 1
                    queue.append((new_i, new_j))
        
        return result