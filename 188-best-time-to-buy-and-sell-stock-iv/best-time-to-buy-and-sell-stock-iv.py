class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        memo = {}
        def dp(i, k, bought):
            if k == 0 or i == len(prices):
                return 0
            
            if (i, k, bought) in memo:
                return memo[(i, k ,bought)]
            
            if bought:
                memo[(i, k ,bought)] = max(dp(i + 1, k - 1, False) + prices[i], dp(i + 1, k, True))
            else:
                memo[(i, k ,bought)] = max(dp(i + 1, k - 1, True) - prices[i], dp(i + 1, k, False))
            
            return memo[(i, k ,bought)]
        
        return dp(0, 2 * k, False)

        

        