import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        total_days = max(e[1] for e in events)
        event_pointer = 0
        heap = []
        attended = 0
        
        for day in range(1, total_days + 1):
            # Add all events starting today
            while event_pointer < len(events) and events[event_pointer][0] == day:
                heapq.heappush(heap, events[event_pointer][1])
                event_pointer += 1
            
            # Remove events that already expired
            while heap and heap[0] < day:
                heapq.heappop(heap)
            
            # Attend the event that ends earliest
            if heap:
                heapq.heappop(heap)
                attended += 1
        
        return attended
