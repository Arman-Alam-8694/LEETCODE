class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=float("-inf")
        fminn=float("inf")
        fmaxx=float("-inf")
        sminn=float("inf")
        one=float("-inf")
        greater=[0]*len(prices)
        rmax=prices[-1]
        for i in range(len(prices)-1,-1,-1):
            rmax=max(rmax,prices[i])
            greater[i]=rmax
        # print(greater)
        for i in range(len(prices)):
            if sminn!=float("-inf") and prices[i]>sminn:
                if one!=float("-inf"):
                    # print(f"one={one},fmin={fminn},fmaxx={fmaxx},sminn={sminn},profit={profit}")
                    # temp=prices[i]-sminn
                    temp1=greater[i]-sminn
                    profit=max(profit,one+temp1)
            if prices[i]<fminn:
                fminn=prices[i]
                sminn=min(sminn,prices[i])
                fmaxx=float("-inf")
            elif prices[i]>fmaxx:
                fmaxx=prices[i]
            else:
                sminn=min(sminn,prices[i])
            

            if fmaxx!=float("-inf") and fmaxx-fminn>one:
                one=fmaxx-fminn
                sminn=prices[i]
        
        profit=max(profit,one)
        # print(profit)
        return profit if profit!=float("-inf") else 0

        

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # fminn: best price seen so far for first buy
#         # one   : max profit after first sell
#         # sminn : effective cost for second buy (price minus first profit)
#         # profit: max profit after second sell
#         fminn = float('inf')
#         one   = 0
#         sminn = float('inf')
#         profit= 0

#         for p in prices:
#             # first buy at lowest price
#             fminn = min(fminn, p)
#             # first sell for max profit
#             one   = max(one,   p - fminn)
#             # second buy at lowest effective cost
#             sminn = min(sminn, p - one)
#             # second sell for max combined profit
#             profit= max(profit,p - sminn)

#         return profit

        