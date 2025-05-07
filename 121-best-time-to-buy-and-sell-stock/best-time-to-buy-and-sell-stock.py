class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn=prices[0]
        profit=0
        for i in prices:
            minn=min(minn,i)
            profit=max(profit,i-minn)
        return profit