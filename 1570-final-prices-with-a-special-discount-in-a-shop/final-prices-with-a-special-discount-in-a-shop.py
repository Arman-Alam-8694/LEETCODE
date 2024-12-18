class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)
        comp=0
        for pos in range(n):
            comp=pos
            while (comp<n and prices[comp]>prices[pos]) or (comp==pos):
                comp+=1
            if comp>=n:
                continue
            else:
                prices[pos]-=prices[comp]
        return prices

               

        