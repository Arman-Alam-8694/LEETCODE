from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if not prices or k == 0:
            return 0
        # unlimited‐txn shortcut
        if k >= n//2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n-1))

        # 1) Build suffix‐max so greater[i] = max(prices[i:])
        greater = [0]*n
        m = 0
        for i in range(n-1, -1, -1):
            m = max(m, prices[i])
            greater[i] = m

        # 2) Sweep left to compute left[i] = best profit with ≤ (k-1) txns in prices[0..i]
        left = [0]*n
        # We'll do a tiny DP for up to (k-1) transactions,
        # but all we ever store per day is the combined max (no suffix‐max or extra arrays later).
        cost = [float('inf')] * k    # cost[j] for j-th buy of the first k-1 trades
        profit = [0] * k             # profit[j] for j-th sell, j=1..k-1 in profit[1..k-1]

        for i, p in enumerate(prices):
            # update DP for the first (k-1) transactions
            for j in range(1, k):
                # “buy j-th time” at net cost = price − profit of previous (j-1) sells
                cost[j] = min(cost[j], p - profit[j-1])
                # “sell j-th time” at price p
                profit[j] = max(profit[j], p - cost[j])
            left[i] = profit[k-1]   # after day i, best you can do with k-1 sells

        # 3) Now combine: for *each* day i as your *k-th* buy & (future) sell
        ans = left[-1]  # maybe you never do the k-th txn at all
        for i, p in enumerate(prices):
            prev = left[i-1] if i > 0 else 0
            # buy k-th at p, sell k-th at the best future price ≥ i, which is greater[i]
            ans = max(ans, prev + (greater[i] - p))

        return ans
