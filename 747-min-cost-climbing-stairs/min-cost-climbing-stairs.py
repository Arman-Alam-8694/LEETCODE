class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def recur(x):
            if x>=len(cost):
                return 0
            if x==-1:
                costt=0
            else:
                costt=cost[x]
            step=min(costt+recur(x+1),costt+recur(x+2))
            return step
        
        return recur(-1)
        