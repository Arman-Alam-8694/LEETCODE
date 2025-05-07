from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if not prices or k == 0:
            return 0
        # shortcut for “unlimited” trades
        if k >= n//2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n-1))

        # 1) build suffix-max so greater[i] = max(prices[i:])
        greater = [0]*n
        m = 0
        for i in range(n-1, -1, -1):
            m = max(m, prices[i])
            greater[i] = m

        # 2) cost[j] = min “effective buy” cost for j-th buy
        #    profit[j] = best profit after j-th sell
        cost   = [float('inf')] * (k+1)
        profit = [0]               * (k+1)

        for i, p in enumerate(prices):
            # a) update the first k–1 trades *in reverse* so we don't
            #    accidentally reuse today’s updated state:
            for j in range(k-1, 0, -1):
                cost[j]   = min(cost[j],   p - profit[j-1])
                # normal “sell today” for trades 1..k-1
                profit[j] = max(profit[j], p - cost[j])

            # b) now handle the k-th transaction using your future-sell trick:
            cost[k]   = min(cost[k],   p - profit[k-1])
            profit[k] = max(profit[k], greater[i] - cost[k])

        return profit[k]
