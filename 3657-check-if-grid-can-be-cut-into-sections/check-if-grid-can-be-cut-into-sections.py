class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def calculate(rectangles, index_start, index_end):
            rectangles.sort(key=lambda x: x[index_start])
            count = 0
            segment_count = 0
            prev_coord = rectangles[0][index_start]
            max_val = float("-inf")
            min_val = float("inf")
            prev_max = -1

            for rect in rectangles:
                if prev_coord != rect[index_start]:
                    if prev_max != -1 and prev_max < max_val:
                        count += max_val - prev_max
                        if min_val >= prev_max:
                            segment_count += 1

                    if prev_max == -1:
                        count += max_val
                        if min_val >= prev_max:
                            segment_count += 1

                    prev_max = max(prev_max, max_val)
                    prev_coord = rect[index_start]
                    min_val = prev_coord

                max_val = max(max_val, rect[index_end])
                min_val = min(min_val, rect[index_start])

            if max_val > prev_max:
                count += max_val - prev_max
                if min_val >= prev_max:
                    segment_count += 1

            return count, segment_count, max_val

        y_count, y_segments, y_max = calculate(rectangles, 1, 3)
        if y_count == y_max and y_segments >= 3:
            return True

        x_count, x_segments, x_max = calculate(rectangles, 0, 2)
        if x_count == x_max and x_segments >= 3:
            return True

        return False

                
            
        
        
        