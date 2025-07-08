from bisect import bisect_left
from functools import lru_cache

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort by start time
        events.sort()
        n = len(events)
        
        # Build list of start times for binary search
        start_times = [e[0] for e in events]

        @lru_cache(None)
        def dp(i, remaining):
            if i == n or remaining == 0:
                return 0
            
            # Option 1: Skip event i
            skip = dp(i + 1, remaining)
            
            # Option 2: Take event i
            # Find next event starting after events[i][1]
            next_i = bisect_left(start_times, events[i][1] + 1)
            take = events[i][2] + dp(next_i, remaining - 1)
            
            return max(skip, take)
        
        return dp(0, k)
