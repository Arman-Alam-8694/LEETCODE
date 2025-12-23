class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        import heapq

        events.sort(key=lambda x: x[0])  # sort by start time
        heap = []                        # (end, value)
        best = 0
        maxx = 0

        for s, e, v in events:
            # release events that ended before s
            while heap and heap[0][0] < s:
                end, val = heapq.heappop(heap)
                maxx = max(maxx, val)

            # take current event alone or with best ended one
            best = max(best, v, v + maxx)

            # add current event
            heapq.heappush(heap, (e, v))

        return best
