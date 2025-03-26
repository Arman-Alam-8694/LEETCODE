class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten grid into array
        array = []
        m = len(grid)
        n = len(grid[0])
        base_remainder = grid[0][0] % x
        for i in range(m):
            for j in range(n):
                if grid[i][j]%x!=base_remainder:
                    return -1
                array.append(grid[i][j])
        
        # Check congruence modulo x
        # if len(array) > 1:  # Only check if more than one element
        #     base_remainder = array[0] % x
        #     for num in array[1:]:
        #         if num % x != base_remainder:
        #             return -1
        
        # If congruent, proceed with binary search
        def check(midd, array):
            cnt = 0
            for y in array:
                if y == midd:
                    continue
                temp = abs(y - midd)
                if temp % x == 0:  # This is guaranteed now, but keep for clarity
                    cnt += (temp // x)
                else:
                    return -1  # Won’t happen due to congruence check
            return cnt
        
        array.sort()
        start = 0
        end = len(array) - 1
        mini = float("inf")
        while start <= end:
            mid = (start + end) // 2
            res = check(array[mid], array)
            if res == -1:
                start = mid + 1  # Move right if impossible (rare now)
            else:
                if res < mini:
                    mini = res
                end = mid - 1  # Try lower values for fewer operations
        
        return mini if mini != float("inf") else -1
