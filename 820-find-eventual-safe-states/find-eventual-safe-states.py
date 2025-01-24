from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        nodes = len(graph)
        safe_nodes = set(x for x in range(nodes) if graph[x] == [])
        visited = set()  # Used to detect cycles in the current DFS traversal

        def dfs(start):
            if start in visited:  # Cycle detected
                return False
            if start in safe_nodes:  # Already confirmed safe
                return True

            visited.add(start)  # Mark as visiting
            for neighbor in graph[start]:
                if not dfs(neighbor):  # If any neighbor is unsafe
                    visited.remove(start)  # Backtrack before returning
                    return False

            visited.remove(start)  # Backtrack
            safe_nodes.add(start)  # Mark as safe
            return True

        result = []
        for i in range(nodes):
            if dfs(i):
                result.append(i)

        return sorted(result)  # Safe nodes should be returned in sorted order
