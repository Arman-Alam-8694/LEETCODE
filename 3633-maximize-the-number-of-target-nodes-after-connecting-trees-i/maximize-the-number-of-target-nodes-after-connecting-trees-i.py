from collections import defaultdict, deque
from typing import List
from functools import lru_cache

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        tree_one = defaultdict(list)
        tree_two = defaultdict(list)
        
        for u, v in edges1:
            tree_one[u].append(v)
            tree_one[v].append(u)
        for u, v in edges2:
            tree_two[u].append(v)
            tree_two[v].append(u)

        def bfs(start, depth, tree):
            count = 0
            queue = deque([(start, 0)])
            seen = {start}
            while queue:
                node, level = queue.popleft()
                count += 1
                if level == depth:
                    continue
                for nei in tree[node]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append((nei, level + 1))
            return count

        # Cache results for tree_two (used only for max)
        second = 0
        if k > 0:
            second = max(bfs(i, k - 1, tree_two) for i in tree_two)

        # Now compute for each node in tree_one
        max_node = max(tree_one) if tree_one else 0
        result = []
        for i in range(max_node + 1):
            if i in tree_one:
                val = bfs(i, k, tree_one)
                result.append(val + second)
            else:
                result.append(second)  # node i is not in the tree, contributes 0
        return result
