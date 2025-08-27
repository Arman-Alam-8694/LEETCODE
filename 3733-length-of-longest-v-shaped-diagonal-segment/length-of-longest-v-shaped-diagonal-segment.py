from functools import cache
from typing import List

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        ans = 0

        def inb(r, c):
            return 0 <= r < row and 0 <= c < col

        visiting = set()

        # diagonal directions in clockwise order
        dirs = [(-1, 1), (1, 1), (1, -1), (-1, -1)]  # UR, DR, DL, UL

        @cache
        def recur(r, c, d, turn):
            """
            Start from (r,c) which is either 2 or 0.
            d = current diagonal direction (0..3).
            turn = 1 if still allowed to turn once clockwise, else 0.
            """
            state = (r, c, d)
            if state in visiting:
                return 0  # avoid infinite loops
            visiting.add(state)

            curr = grid[r][c]
            need = 0 if curr == 2 else 2
            best = 1  # count current cell

            # continue straight
            dr, dc = dirs[d]
            nr, nc = r + dr, c + dc
            if inb(nr, nc) and grid[nr][nc] == need:
                best = max(best, 1 + recur(nr, nc, d, turn))

            # one clockwise turn
            if turn:
                nd = (d + 1) % 4
                dr2, dc2 = dirs[nd]
                nr2, nc2 = r + dr2, c + dc2
                if inb(nr2, nc2) and grid[nr2][nc2] == need:
                    best = max(best, 1 + recur(nr2, nc2, nd, 0))

            visiting.remove(state)   # ✅ important: allow reuse in other paths
            return best

        # start only from 1 → diagonally into 2
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    ans = max(ans, 1)  # at least just '1'
                    for d, (dr, dc) in enumerate(dirs):
                        ni, nj = i + dr, j + dc
                        if inb(ni, nj) and grid[ni][nj] == 2:
                            ans = max(ans, 1 + recur(ni, nj, d, 1))

        return ans
