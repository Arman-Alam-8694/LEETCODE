import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]],
                          src: int, dst: int, k: int) -> int:
        k += 1

        adj = [[] for _ in range(n)]
        for u, v, cost in flights:
            adj[u].append((v, cost))

        heap = [(0, 0, src)]  
        best_steps = [float('inf')] * n

        while heap:
            cost, steps, node = heapq.heappop(heap)

            if steps > k:
                continue

            if node == dst:
                return cost

            if steps >= best_steps[node]:
                continue

            best_steps[node] = steps

            for nei, price in adj[node]:
                heapq.heappush(heap, (cost + price, steps + 1, nei))

        return -1
