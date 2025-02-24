from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        from collections import defaultdict

        # Step 1: Build adjacency list (tree)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Step 2: Find the path from Bob to 0
        parent = {}  
        bob_path_time = {}  # Track when Bob reaches each node
        bob_time = 0
        
        def find_bob_path(node, par, time):
            """Find Bob's path from bob → 0 and store arrival times."""
            parent[node] = par
            bob_path_time[node] = time
            if node == 0:
                return True  # Found root, stop recursion
            
            for neighbor in graph[node]:
                if neighbor != par and find_bob_path(neighbor, node, time + 1):
                    return True
            del bob_path_time[node]  # Not in Bob's path
            return False
        
        find_bob_path(bob, -1, 0)

        # Step 3: DFS for Alice's most profitable path
        max_profit = float('-inf')

        def dfs(alice, parent, time, profit):
            """DFS for Alice to maximize profit."""
            nonlocal max_profit

            # Determine Alice's net earnings at this node
            if alice in bob_path_time:
                bob_arrival = bob_path_time[alice]
                if bob_arrival == time:  # Meet at the same time → split
                    profit += amount[alice] // 2
                elif bob_arrival > time:  # Alice arrives first → full profit
                    profit += amount[alice]
            else:  # Bob never comes here → Alice gets full amount
                profit += amount[alice]

            # If it's a leaf node (except root), update max_profit
            if alice != 0 and len(graph[alice]) == 1:
                max_profit = max(max_profit, profit)
                return

            # Continue DFS for Alice
            for neighbor in graph[alice]:
                if neighbor != parent:
                    dfs(neighbor, alice, time + 1, profit)

        dfs(0, -1, 0, 0)
        return max_profit
