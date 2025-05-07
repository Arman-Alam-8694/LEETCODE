class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minn=float("inf")
        maxx=float("-inf")
        for p in prices:
            if maxx!=float("-inf") and p<maxx:
                profit+=maxx-minn
                minn=float("inf")
                maxx=float("-inf")
            minn=min(minn,p)
            maxx=max(maxx,p)
        profit+=maxx-minn
        return profit


        