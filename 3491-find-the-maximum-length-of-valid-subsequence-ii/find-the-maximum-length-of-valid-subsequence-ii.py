class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp=[[0]*k for _ in range(k)]
        answer=0
        for num in nums:
            num%=k
            for prev in range(k):
                dp[num][prev]=dp[prev][num]+1
        for i in range(k):
            for j in range(k):
                answer=max(answer,dp[i][j])
        return answer