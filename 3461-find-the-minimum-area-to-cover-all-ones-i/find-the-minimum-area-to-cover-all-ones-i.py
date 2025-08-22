from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # handle empty
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        # total ones count
        ones = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ones += 1
        if ones == 0:
            return 0

        # 1) largest square DP (size = side length)
        dp = [[0]*n for _ in range(m)]
        max_square_size = 0
        max_square_bottom_right = (-1, -1)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
                    if dp[r][c] > max_square_size:
                        max_square_size = dp[r][c]
                        max_square_bottom_right = (r, c)

        # If the largest square covers all ones (i.e., it's a filled square equal to total ones),
        # then that square is the minimal covering rectangle (area = side^2).
        if max_square_size * max_square_size == ones:
            return max_square_size * max_square_size

        # 2) longest consecutive ones in any row / column (to detect 1 x n or n x 1)
        max_row_run = 0
        for r in range(m):
            cur = 0
            for c in range(n):
                if grid[r][c] == 1:
                    cur += 1
                    if cur > max_row_run:
                        max_row_run = cur
                else:
                    cur = 0

        max_col_run = 0
        for c in range(n):
            cur = 0
            for r in range(m):
                if grid[r][c] == 1:
                    cur += 1
                    if cur > max_col_run:
                        max_col_run = cur
                else:
                    cur = 0

        # If all ones lie on a single row or single column (i.e., the longest run equals total ones),
        # the minimal covering rectangle area is exactly number of ones (1 x ones or ones x 1).
        if max_row_run == ones or max_col_run == ones:
            return ones

        # 3) fallback: compute minimal axis-aligned bounding rectangle (guaranteed correct)
        min_r, max_r = m, -1
        min_c, max_c = n, -1
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if r < min_r: min_r = r
                    if r > max_r: max_r = r
                    if c < min_c: min_c = c
                    if c > max_c: max_c = c

        height = max_r - min_r + 1
        width = max_c - min_c + 1
        return height * width
