class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(1, len(edges) + 1)}

        def dfs(node, parent):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, node):  # Continue DFS
                        return True
                elif neighbor != parent:
                    # If the neighbor is already visited and it's not the parent, we've found a cycle
                    return True
            return False

        # Add edges to the graph
        for edge in edges:
            # Build the graph as an adjacency list
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)

            visited = [False] * (len(edges) + 1)
            if dfs(a, -1):  # Start DFS from node a
                return edge  # Return the edge that forms the cycle
