import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # 1. Always sort meetings by start time
        meetings.sort()
        
        # 2. Track which rooms are free (min-heap for smallest index)
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        
        # 3. Track ongoing meetings (min-heap of [end_time, room_index])
        used_rooms = [] 
        
        # 4. Result tracking
        booking_count = [0] * n
        
        for start, end in meetings:
            # Step A: Free up rooms where the meeting has finished
            while used_rooms and used_rooms[0][0] <= start:
                _, room_idx = heapq.heappop(used_rooms)
                heapq.heappush(free_rooms, room_idx)
            
            # Step B: If no room is free, the meeting is delayed
            if not free_rooms:
                earliest_end, room_idx = heapq.heappop(used_rooms)
                # The delayed meeting starts when the room is free
                # duration remains (end - start)
                new_end = earliest_end + (end - start)
                heapq.heappush(used_rooms, [new_end, room_idx])
                booking_count[room_idx] += 1
            
            # Step C: If a room is free, take the one with the smallest index
            else:
                room_idx = heapq.heappop(free_rooms)
                heapq.heappush(used_rooms, [end, room_idx])
                booking_count[room_idx] += 1
                
        # Return the room index with max bookings (handle ties by returning smallest index)
        return booking_count.index(max(booking_count))