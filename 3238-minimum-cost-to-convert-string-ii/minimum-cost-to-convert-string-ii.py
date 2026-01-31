from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        
        # 1. Identify all unique strings and map them to IDs
        # We need this to build our adjacency matrix for Floyd-Warshall
        unique_strs = list(set(original) | set(changed))
        str_to_id = {s: i for i, s in enumerate(unique_strs)}
        m = len(unique_strs)
        
        # 2. Initialize the distance matrix with infinity
        # dist[i][j] will store the min cost to transform string ID i to string ID j
        dist = [[float('inf')] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0
            
        # 3. Fill the matrix with the direct transformation costs provided
        for o, c, z in zip(original, changed, cost):
            u, v = str_to_id[o], str_to_id[c]
            dist[u][v] = min(dist[u][v], z)
            
        # 4. Floyd-Warshall: Find shortest paths between all pairs of strings
        # This handles sequences like A -> B -> C
        for k in range(m):
            for i in range(m):
                # Optimization: if dist[i][k] is inf, no need to check j
                if dist[i][k] == float('inf'): continue 
                for j in range(m):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # 5. Dynamic Programming to find the min cost for the entire string
        # dp[i] = minimum cost to convert source[0...i-1] to target[0...i-1]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Pre-collect unique lengths of transformation rules to avoid checking all 1..1000
        valid_lengths = sorted(list(set(len(s) for s in original)))
        
        for i in range(n):
            if dp[i] == float('inf'):
                continue
            
            # Case 1: The current characters already match
            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])
            
            # Case 2: Try every possible transformation length starting at index i
            for length in valid_lengths:
                if i + length > n:
                    break
                
                sub_s = source[i : i + length]
                sub_t = target[i : i + length]
                
                # If both substrings exist in our map, check the transformation cost
                if sub_s in str_to_id and sub_t in str_to_id:
                    u, v = str_to_id[sub_s], str_to_id[sub_t]
                    if dist[u][v] != float('inf'):
                        dp[i + length] = min(dp[i + length], dp[i] + dist[u][v])
                        
        return dp[n] if dp[n] != float('inf') else -1