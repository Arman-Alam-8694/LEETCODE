import heapq
from collections import defaultdict

class Solution:
    def avoidFlood(self, rains):
        n = len(rains)
        ans = []
        next_rain = defaultdict(list)
        
        # Precompute all rain days for each lake
        for i, lake in enumerate(rains):
            if lake > 0:
                next_rain[lake].append(i)
        
        full_lakes = set()
        heap = []  # (nextRainDay, lake)
        
        for i, lake in enumerate(rains):
            if lake > 0:
                if lake in full_lakes:
                    return []  # flood!
                full_lakes.add(lake)
                next_rain[lake].pop(0)
                if next_rain[lake]:  # if it rains again
                    heapq.heappush(heap, (next_rain[lake][0], lake))
                ans.append(-1)
            else:
                if heap:
                    next_day, lake_to_dry = heapq.heappop(heap)
                    full_lakes.remove(lake_to_dry)
                    ans.append(lake_to_dry)
                else:
                    ans.append(1)
        return ans
