class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1.0

        @lru_cache(None)
        def dp(a, b):
            # Base cases
            if a <= 0 and b <= 0:
                return 0.5  # both finish together
            if a <= 0:
                return 1.0  # A finishes first
            if b <= 0:
                return 0.0  # B finishes first

            # Expected value over all 4 operations
            return 0.25 * (
                dp(a - 100, b) +
                dp(a - 75, b - 25) +
                dp(a - 50, b - 50) +
                dp(a - 25, b - 75)
            )

        return dp(n, n)