from bisect import insort, bisect_left
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        n = len(times)
        
        # Step 1: Create the events (arrival and departure)
        events = []
        for i, (arrive, leave) in enumerate(times):
            events.append((arrive, 'arrive', i))
            events.append((leave, 'leave', i))
        
        # Step 2: Sort the events by time (break ties by giving priority to 'leave' events)
        events.sort(key=lambda x: (x[0], x[1] == 'arrive'))
        
        # Step 3: Initialize list of available chairs
        available_chairs = list(range(n))  # Initially all chairs are available, [0, 1, 2, ..., n-1]
        occupied_chairs = [None] * n       # To track which chair each friend occupies
        
        # Step 4: Process the events
        for time, event_type, friend_id in events:
            if event_type == 'arrive':
                # Find the smallest available chair using binary search (which is the first element of available_chairs)
                chair = available_chairs.pop(0)  # Get the smallest available chair
                occupied_chairs[friend_id] = chair  # Assign this chair to the friend
                
                if friend_id == targetFriend:
                    return chair
            
            elif event_type == 'leave':
                # When a friend leaves, their chair becomes available again
                chair = occupied_chairs[friend_id]
                insort(available_chairs, chair)  # Insert the chair back in the sorted list using binary insertion
        
        return -1  # This should never be reached
