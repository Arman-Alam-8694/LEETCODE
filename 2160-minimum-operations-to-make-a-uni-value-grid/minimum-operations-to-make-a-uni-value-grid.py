class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        def check(midd, array):
            cnt = 0
            for y in array:
                if y == midd:
                    continue
                temp = abs(y - midd)
                if temp % x == 0:
                    cnt += (temp // x)
                else:
                    return -1
            return cnt
        
        array = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                array.append(grid[i][j])
        array.sort()
        start = 0
        end = len(array) - 1
        mini = float("inf")
        while start <= end:
            mid = (start + end) // 2
            res = check(array[mid], array)
            if res == -1:
                start = mid + 1  # Move right if impossible
            else:
                if res < mini:
                    mini = res
                end = mid - 1  # Try lower values for fewer operations
        return mini if mini != float("inf") else -1