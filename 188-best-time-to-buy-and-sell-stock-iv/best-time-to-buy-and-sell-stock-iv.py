class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        # If k >= n/2, same as unlimited transactions
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        # dp[i]: max profit at i-th transaction
        dp = [0] * (k + 1)
        # max_diff[i]: max(dp[i - 1] - prices[j]) seen so far
        max_diff = [-prices[0]] * (k + 1)

        for i in range(1, n):
            for j in range(1, k + 1):
                dp[j] = max(dp[j], prices[i] + max_diff[j])
                max_diff[j] = max(max_diff[j], dp[j - 1] - prices[i])

        return dp[k]
