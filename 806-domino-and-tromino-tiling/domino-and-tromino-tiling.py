class Solution:
    def numTilings(self, n: int) -> int:
        dp=[0]*(n+4)
        MOD=10**9+7
        dp[0]=1
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=(2*dp[i-1]+dp[i-3])%MOD
        return dp[n]