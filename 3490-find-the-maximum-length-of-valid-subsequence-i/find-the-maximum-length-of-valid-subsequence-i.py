class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        k=2
        dp=[[0]*k for _ in range(k)]
        answer=0
        for num in nums:
            num%=k
            for prev in range(k):
                dp[num][prev]=dp[prev][num]+1
                answer=max(answer,dp[num][prev])
        return answer
        