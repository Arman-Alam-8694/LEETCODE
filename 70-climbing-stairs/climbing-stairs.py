class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def recur(n):
            nonlocal dp
            if n<2:
                return 1
            if dp[n]!=-1:
                return dp[n]
            dp[n]=recur(n-1)+recur(n-2)
            return dp[n]
        
        return recur(n)
        
        