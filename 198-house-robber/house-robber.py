class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+1)
        def recur(n):
            if n<=0:
                return 0
            if dp[n]!=-1:
                return dp[n]
            dp[n]=max(recur(n-1),nums[n-1]+recur(n-2))
            return dp[n]
        
        return recur(n)


        