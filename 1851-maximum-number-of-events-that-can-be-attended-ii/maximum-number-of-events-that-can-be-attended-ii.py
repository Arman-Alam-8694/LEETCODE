class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        start_days=[e[0] for e in events]
        n=len(events)
        dp=[[0]*(k+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            start,end,value=events[i]
            for j in range(1,k+1):
                #no-take
                dp[i][j]=dp[i+1][j]
                next_index=bisect_left(start_days,end+1)
                dp[i][j]=max(dp[i][j],value+dp[next_index][j-1])
        return dp[0][k]