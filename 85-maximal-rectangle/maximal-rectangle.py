from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])

        # colP[i][j] = number of consecutive '1's vertically ending at (i, j)
        colP = [[0] * cols for _ in range(rows)]
        # rowP[i][j] = number of consecutive '1's horizontally ending at (i, j)
        rowP = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    colP[i][j] = 1 + (colP[i-1][j] if i > 0 else 0)
                    rowP[i][j] = 1 + (rowP[i][j-1] if j > 0 else 0)
                else:
                    colP[i][j] = 0
                    rowP[i][j] = 0

        ans = 0

        # For each cell (i, j) treat it as the bottom-right corner of a rectangle
        # Use rowP to bound how far left we need to check (upper bound on width)
        for i in range(rows):
            for j in range(cols):
                if colP[i][j] == 0:
                    continue

                min_height = colP[i][j]
                max_width = rowP[i][j]  # upper bound on width (can't be wider than this)

                # expand left (bounded by max_width)
                # k goes from j down to j - max_width + 1
                for k in range(j, j - max_width, -1):
                    # if there's a zero in this column at this row, we can't expand further
                    if colP[i][k] == 0:
                        break

                    # minimum height among columns k..j determines rectangle height
                    if colP[i][k] < min_height:
                        min_height = colP[i][k]

                    width = j - k + 1
                    area = min_height * width
                    if area > ans:
                        ans = area

                    # Optional small pruning: if min_height * max_width <= ans, no larger area
                    # can be produced for this starting min_height; but since min_height may
                    # drop later, pruning must be used carefully. We omit aggressive pruning here.

        return ans
