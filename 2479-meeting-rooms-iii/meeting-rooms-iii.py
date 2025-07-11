class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
    
        # min-heap to keep track of available rooms
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        
        # min-heap to keep track of ongoing meetings as (end_time, room)
        busy_rooms = []

        # count how many meetings each room has hosted
        room_usage = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free up rooms that are done before current meeting's start
            while busy_rooms and busy_rooms[0][0] <= start:
                end_time, room = heapq.heappop(busy_rooms)
                heapq.heappush(available_rooms, room)

            if available_rooms:
                # Assign room with smallest number
                room = heapq.heappop(available_rooms)
                heapq.heappush(busy_rooms, (end, room))
            else:
                # Delay meeting: take the room that gets free the earliest
                end_time, room = heapq.heappop(busy_rooms)
                heapq.heappush(busy_rooms, (end_time + duration, room))
                # simulate delayed start

            room_usage[room] += 1

        # Find the room with max usage (if tie, smallest index)
        max_meetings = max(room_usage)
        for i in range(n):
            if room_usage[i] == max_meetings:
                return i
        