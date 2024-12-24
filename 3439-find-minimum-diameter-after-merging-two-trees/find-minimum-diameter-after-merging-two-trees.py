from heapq import heappush, heappop
from math import ceil
from typing import List

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        adj1 = {}
        adj2 = {}
        
        # Build adjacency list for graph 1
        for u, v in edges1:
            if u not in adj1:
                adj1[u] = []
            if v not in adj1:
                adj1[v] = []
            adj1[u].append(v)
            adj1[v].append(u)
        
        # Build adjacency list for graph 2
        for u, v in edges2:
            if u not in adj2:
                adj2[u] = []
            if v not in adj2:
                adj2[v] = []
            adj2[u].append(v)
            adj2[v].append(u)

        def dfs(node, par, adj):
            max_d = 0
            max_subtree = [0, 0]
            for child in adj.get(node, []):
                if par == child:
                    continue
                mxd, mxch = dfs(child, node, adj)
                max_d = max(max_d, mxd)
                heappush(max_subtree, mxch)
                # Ensure max_subtree contains at most two elements
                if len(max_subtree) > 2:
                    heappop(max_subtree)
            max_d = max(max_d, sum(max_subtree))
            return [max_d, 1 + max(max_subtree)]

        # Calculate diameters for both trees
        d1, _ = dfs(0, -1, adj1)
        d2, _ = dfs(0, -1, adj2)

        # When merging, the maximum possible diameter is formed by connecting the farthest nodes
        # of the two trees, thus adding 1 for the edge that connects them.
        return max(d1, d2, 1 + ceil(d1 / 2) + ceil(d2 / 2))
