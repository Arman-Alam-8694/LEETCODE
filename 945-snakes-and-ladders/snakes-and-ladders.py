class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        min_steps = [float('inf')]  # Acts like a global minimum holder

        # Helper to convert square number to (row, col)
        def get_pos(num):
            r = (num - 1) // n
            c = (num - 1) % n
            if r % 2 == 1:
                c = n - 1 - c
            return n - 1 - r, c

        visited = {}

        def dfs(square, steps):
            if square in visited and visited[square] <= steps:
                return  # Already reached this square in fewer steps
            if steps >= min_steps[0]:
                return  # Prune: already exceeded current best
            visited[square] = steps

            if square == target:
                min_steps[0] = min(min_steps[0], steps)
                return

            for i in range(1, 7):
                next_square = square + i
                if next_square > target:
                    continue
                r, c = get_pos(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                dfs(next_square, steps + 1)

        dfs(1, 0)
        return min_steps[0] if min_steps[0] != float('inf') else -1



        