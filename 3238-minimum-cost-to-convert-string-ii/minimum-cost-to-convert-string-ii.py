import heapq
from collections import defaultdict

class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        n = len(source)
        
        # --- PHASE 1: Build the String Graph & Map to IDs ---
        unique_strs = list(set(original) | set(changed))
        str_to_id = {s: i for i, s in enumerate(unique_strs)}
        m = len(unique_strs)
        
        # Build adjacency list for Dijkstra
        adj = defaultdict(list)
        for o, c, z in zip(original, changed, cost):
            adj[str_to_id[o]].append((str_to_id[c], z))
            
        # Precompute all-pairs shortest paths using Dijkstra for each string
        # We store this in a 2D matrix for O(1) lookup during DP
        min_dist = [[float('inf')] * m for _ in range(m)]
        for start_id in range(m):
            min_dist[start_id][start_id] = 0
            pq = [(0, start_id)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > min_dist[start_id][u]: continue
                for v, weight in adj[u]:
                    if d + weight < min_dist[start_id][v]:
                        min_dist[start_id][v] = d + weight
                        heapq.heappush(pq, (min_dist[start_id][v], v))
        
        # --- PHASE 2: Build the Trie for fast substring matching ---
        # Each node in the Trie stores the ID of the string ending there
        trie = {}
        for s, s_id in str_to_id.items():
            curr = trie
            for char in s:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['#'] = s_id # '#' marks the end of a valid transformation string

        # --- PHASE 3: Linear DP with Trie Traversal ---
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == float('inf'): continue
            
            # Choice 1: Skip if characters match
            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])
            
            # Choice 2: Find all valid transformations starting at index i
            # We traverse source and target simultaneously down the Trie
            node_s = trie
            node_t = trie
            
            # We only need to check lengths present in the original rules
            # We walk both source[i...] and target[i...] through the Trie
            # If both reach a valid terminal node ('#'), we have a transformation
            for j in range(i, n):
                char_s = source[j]
                char_t = target[j]
                
                # If either path breaks in the Trie, no more transformations possible at this start index
                if char_s not in node_s or char_t not in node_t:
                    break
                
                node_s = node_s[char_s]
                node_t = node_t[char_t]
                
                # If both substrings are "known" strings (present in original/changed)
                if '#' in node_s and '#' in node_t:
                    id_s = node_s['#']
                    id_t = node_t['#']
                    cost_val = min_dist[id_s][id_t]
                    
                    if cost_val != float('inf'):
                        dp[j + 1] = min(dp[j + 1], dp[i] + cost_val)
                        
        return dp[n] if dp[n] != float('inf') else -1