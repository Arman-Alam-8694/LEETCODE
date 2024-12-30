class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp={}
        def recur(x):
            if x>=len(cost):
                return 0
            if x in dp:
                return dp[x]
            if x==-1:
                costt=0
            else:
                costt=cost[x]
            step=min(costt+recur(x+1),costt+recur(x+2))
            dp[x]=step
            return dp[x]
        
        return recur(-1)
        