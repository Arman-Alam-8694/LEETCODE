class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[-1]*m for _ in range(n)]
        def recur(a,b):
            if a==-1 or b==-1:
                return 0
            if dp[a][b]!=-1:
                return dp[a][b]
            if text1[a]==text2[b]:
                dp[a][b]=1+recur(a-1,b-1)
                return dp[a][b]
            dp[a][b]=max(recur(a-1,b),recur(a,b-1))
            return dp[a][b]
        return recur(n-1,m-1)