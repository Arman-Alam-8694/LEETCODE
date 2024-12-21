class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        # dp[i][j] will store a dictionary where the key is XOR value and the value is the count of paths that result in that XOR.
        dp = [[{} for _ in range(n)] for _ in range(m)]
        
        # Initialize the starting point (0, 0)
        dp[0][0][grid[0][0]] = 1
        
        # Iterate through the grid
        for i in range(m):
            for j in range(n):
                for xor_val, count in dp[i][j].items():
                    # Move down if possible
                    if i + 1 < m:
                        new_xor = xor_val ^ grid[i + 1][j]
                        dp[i + 1][j][new_xor] = (dp[i + 1][j].get(new_xor, 0) + count) % MOD
                    
                    # Move right if possible
                    if j + 1 < n:
                        new_xor = xor_val ^ grid[i][j + 1]
                        dp[i][j + 1][new_xor] = (dp[i][j + 1].get(new_xor, 0) + count) % MOD
        
        # Return the number of paths that reach (m-1, n-1) with XOR value equal to k
        return dp[m - 1][n - 1].get(k, 0)
            