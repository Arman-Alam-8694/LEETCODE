class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        min_heap=[]
        i,day=0,0
        n=len(events)
        result=0
        while i<n or min_heap:
            if not min_heap:
                day=events[i][0]
            while i<n and (events[i][0]<=day and events[i][1]>=day):
                heapq.heappush(min_heap,events[i][1])
                i+=1
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            if min_heap:
                heapq.heappop(min_heap)
                day+=1
                result+=1
            else:
                day+=1
        return result
            
