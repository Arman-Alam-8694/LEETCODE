class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(words[0]), len(target)

        # Precompute frequency of characters in each column
        freq = [Counter() for _ in range(m)]
        for word in words:
            for i, char in enumerate(word):
                freq[i][char] += 1

        # Initialize DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1  # Base case: one way to form an empty target using no columns

        # Fill DP table
        for i in range(1, m + 1):  # Iterate over columns
            for j in range(n + 1):  # Iterate over target characters
                # Carry forward ways without using this column
                dp[i][j] = dp[i - 1][j]
                if j > 0:  # If forming at least one character of the target
                    char = target[j - 1]
                    dp[i][j] += dp[i - 1][j - 1] * freq[i - 1][char]
                    dp[i][j] %= MOD

        return dp[m][n]




        

        