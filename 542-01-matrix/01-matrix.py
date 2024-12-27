from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        result = [[float('inf')] * col for _ in range(row)]
        queue = deque()
        visited = set()  # Add visited set
        
        # First pass: Find all 0s
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))
                    visited.add((i, j))  # Mark zeros as visited
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            curr_i, curr_j = queue.popleft()
            curr_dist = result[curr_i][curr_j]
            
            for di, dj in directions:
                new_i, new_j = curr_i + di, curr_j + dj
                
                if (0 <= new_i < row and 
                    0 <= new_j < col and 
                    (new_i, new_j) not in visited):  # Check if not visited
                    result[new_i][new_j] = curr_dist + 1
                    queue.append((new_i, new_j))
                    visited.add((new_i, new_j))  # Mark as visited
        
        return result