class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        def dfs(node, parent):
            nonlocal cnt
            current_sum = values[node] % k  # Start with the value of the current node
            divisible_count = 0  # Count of divisible components

            for neighbor in graph[node]:
                if neighbor != parent:  # Avoid revisiting the parent node
                    child_sum, child_divisible_count = dfs(neighbor, node)
                    divisible_count += child_divisible_count  # Add child counts
                    current_sum += child_sum  # Add child sum to current node

            # Check if the current subtree is divisible
            if current_sum % k == 0:
                divisible_count += 1  # This subtree forms a component
                return 0, divisible_count  # Return 0 as the sum for the parent
            return current_sum, divisible_count  # Return current sum and count

        # Build the graph from edges
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize variables
        cnt = 0

        # Start DFS from node 0
        _, cnt = dfs(0, -1)
        return cnt
