from collections import defaultdict

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        def dfs(node, parent):
            csumm = values[node]
            for son in graph[node]:
                if son != parent:
                    csumm += dfs(son, node)

            # If the sum is divisible by k, reset it to 0 and increment the count
            if csumm % k == 0:
                self.divisible_count += 1
                return 0
            return csumm

        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.divisible_count = 0
        dfs(0, -1)
        return self.divisible_count
