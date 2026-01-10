import sys

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # 1. Increase recursion limit for N = 1000
        # sys.setrecursionlimit(2000)
        
        # 2. Sort to handle age constraints
        players = sorted(zip(ages, scores))
        n = len(players)
        
        # 3. Initialize manual memo table with -1 (meaning "not yet calculated")
        # Shape: [n][n + 1] to account for prev_idx = -1
        memo = [[-1] * (n + 1) for _ in range(n)]

        def solve(idx, prev_idx):
            if idx == n:
                return 0
            
            # Map prev_idx (-1 to n-1) to (0 to n) for array indexing
            memo_col = prev_idx + 1
            
            if memo[idx][memo_col] != -1:
                return memo[idx][memo_col]
            
            # Option 1: Skip current player
            res = solve(idx + 1, prev_idx)
            
            # Option 2: Pick current player (if score is non-decreasing)
            curr_score = players[idx][1]
            if prev_idx == -1 or curr_score >= players[prev_idx][1]:
                res = max(res, curr_score + solve(idx + 1, idx))
            
            # Save and return
            memo[idx][memo_col] = res
            return res

        return solve(0, -1)