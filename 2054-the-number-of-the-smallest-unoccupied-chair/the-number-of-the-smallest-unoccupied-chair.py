class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        def binary_search_insert(chairs, chair):
            """Use binary search to insert chair in the sorted list of available chairs."""
            left, right = 0, len(chairs)
            while left < right:
                mid = (left + right) // 2
                if chairs[mid] < chair:
                    left = mid + 1
                else:
                    right = mid
            chairs.insert(left, chair)  # Insert at the correct position
        
        
        n = len(times)
        # Step 1: Create events for arrivals and leavings
        events = []
        for i, (arrive, leave) in enumerate(times):
            events.append((arrive, 'arrive', i))  # Arrival event
            events.append((leave, 'leave', i))    # Leaving event
        
        # Step 2: Sort events by time (and prioritize 'leave' over 'arrive' if they have the same time)
        events.sort(key=lambda x: (x[0], x[1] == 'arrive'))
        
        # Step 3: Initialize available chairs and a dictionary to track occupied chairs
        available_chairs = list(range(n))  # Initially all chairs are available
        occupied_chairs = {}
        
        # Step 4: Process each event
        for time, event_type, friend_id in events:
            if event_type == 'arrive':
                # Binary search to find the smallest available chair (it's at index 0)
                chair = available_chairs.pop(0)  # Remove the first element (smallest chair)
                occupied_chairs[friend_id] = chair
                if friend_id == targetFriend:
                    return chair
            else:
                # Friend is leaving, add their chair back using binary search insert
                chair = occupied_chairs[friend_id]
                binary_search_insert(available_chairs, chair)
        
        return -1  # This should never be reached
