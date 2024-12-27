class Solution:
    def climbStairs(self, n: int) -> int:
        def recur(n,dp):
            # nonlocal dp
            if n<2:
                return 1
            if dp[n]!=-1:
                return dp[n]
            dp[n]=recur(n-1,dp)+recur(n-2,dp)
            return dp[n]
        
        dp=[-1]*(n+1)
        return recur(n,dp)
        
        