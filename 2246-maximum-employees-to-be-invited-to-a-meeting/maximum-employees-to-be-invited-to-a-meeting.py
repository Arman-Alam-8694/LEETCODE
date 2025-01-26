from collections import deque
from typing import List

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)  # Number of nodes
        deg = [0] * n  # Array to store the in-degree of each node
        
        # Compute in-degrees for each node
        for f in favorite:
            deg[f] += 1 
        
        # Initialize max_depth for each node and the queue for topological sort
        max_depth = [1] * n
        q = deque(i for i, d in enumerate(deg) if d == 0)  # Nodes with 0 in-degree
        
        # Perform topological sort to compute max_depth for each node
        while q:
            x = q.popleft()
            y = favorite[x]
            max_depth[y] = max_depth[x] + 1  # Update depth of the favorite node
            deg[y] -= 1  # Decrease in-degree of the favorite node
            if deg[y] == 0:
                q.append(y)
        
        # Variables to track the maximum cycle size and chain sizes
        max_ring_size = sum_chain_size = 0
        
        # Detect cycles and calculate sizes
        for i, d in enumerate(deg):
            if d == 0:
                continue  # Skip nodes already processed
            
            # Start cycle detection for node i
            deg[i] = 0  # Mark node as visited
            ring_size = 1  # Initialize cycle size
            x = favorite[i]
            
            while x != i:  # Traverse the cycle
                deg[x] = 0  # Mark node as visited
                ring_size += 1
                x = favorite[x]
            
            if ring_size == 2:  # Special case: cycle of size 2
                sum_chain_size += max_depth[i] + max_depth[favorite[i]]
            else:
                max_ring_size = max(max_ring_size, ring_size)  # Update max cycle size
        
        # Return the maximum value between the largest cycle or the sum of chains
        return max(max_ring_size, sum_chain_size)