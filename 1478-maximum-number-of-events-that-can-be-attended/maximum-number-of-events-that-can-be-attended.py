class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])  # Greedy on end time
        max_day = max(end for _, end in events)
        
        parent = list(range(max_day + 2))  # DSU: parent[i] = next available day ≥ i

        def find(day):
            if parent[day] != day:
                parent[day] = find(parent[day])
            return parent[day]

        count = 0
        for start, end in events:
            day = find(start)
            if day <= end:
                count += 1
                parent[day] = find(day + 1)  # Mark day as used

        return count
