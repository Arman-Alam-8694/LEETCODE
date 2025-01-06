class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        path = [["."] * n for _ in range(n)]
        result = []

        def dfs(row, cnt, visited):
            if cnt == n:
                result.append(["".join(row) for row in path])
                return

            for i in range(n):
                if (row, i) not in visited:
                    # Place the queen
                    path[row][i] = "Q"

                    # Make a copy of the visited set
                    new_visited = visited.copy()
                    for j in range(n):
                        # Mark row and column
                        new_visited.add((row, j))
                        new_visited.add((j, i))
                        # Mark diagonals
                        if row + j < n and i + j < n:
                            new_visited.add((row + j, i + j))
                        if row + j < n and i - j >= 0:
                            new_visited.add((row + j, i - j))
                        if row - j >= 0 and i + j < n:
                            new_visited.add((row - j, i + j))
                        if row - j >= 0 and i - j >= 0:
                            new_visited.add((row - j, i - j))

                    # Recursive call to the next row
                    dfs(row + 1, cnt + 1, new_visited)

                    # Backtrack
                    path[row][i] = "."

        # Initial call with an empty visited set
        dfs(0, 0, set())
        return result
