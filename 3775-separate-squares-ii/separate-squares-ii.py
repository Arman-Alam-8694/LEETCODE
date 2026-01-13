from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []  # (y, type, x1, x2)

        # Step 1: build y-events
        for x, y, l in squares:
            events.append((y, 1, x, x + l))      # square enters
            events.append((y + l, -1, x, x + l)) # square leaves

        # sort events by y
        events.sort()

        # Step 2: compute total union area (for target)
        active = []
        total_area = 0.0

        def union_x_length(intervals):
            if not intervals:
                return 0.0
            intervals.sort()
            length = 0.0
            cur_l, cur_r = intervals[0]
            for l, r in intervals[1:]:
                if l > cur_r:
                    length += cur_r - cur_l
                    cur_l, cur_r = l, r
                else:
                    cur_r = max(cur_r, r)
            length += cur_r - cur_l
            return length

        # first sweep to get total union area
        for i in range(len(events) - 1):
            y, typ, x1, x2 = events[i]
            if typ == 1:
                active.append((x1, x2))
            else:
                active.remove((x1, x2))

            next_y = events[i + 1][0]
            height = next_y - y
            if height > 0:
                total_area += union_x_length(active) * height

        target = total_area / 2.0

        # Step 3: second sweep to find answer y
        active.clear()
        area_so_far = 0.0

        for i in range(len(events) - 1):
            y, typ, x1, x2 = events[i]
            if typ == 1:
                active.append((x1, x2))
            else:
                active.remove((x1, x2))

            next_y = events[i + 1][0]
            height = next_y - y
            if height <= 0:
                continue

            cur_width = union_x_length(active)
            slab_area = cur_width * height

            if area_so_far + slab_area >= target:
                # interpolate inside this slab
                remaining = target - area_so_far
                return y + remaining / cur_width

            area_so_far += slab_area

        return 0.0
