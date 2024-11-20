class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        minn=prices[0]
        profit=0
        for i in range(1,n):
            # print(minn)
            if prices[i-1]>prices[i]:
               
                profit+=prices[i-1]-minn
                minn=prices[i]
            else:
                minn=min(minn,prices[i])
        if len(prices)>=2 and (prices[-1]>=prices[-2]):
            profit+=prices[-1]-minn
        return profit
        