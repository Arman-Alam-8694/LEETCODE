class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        size=len(nums)
        dp=[-1]*(n+1)
        def recur(n,size):
            if n<=0:
                return 0
            if dp[n]!=-1:
                return dp[n]
            temp=float('-inf')
            for i in range(2,size+2):
                if n-i>=-1:
                    temp=max(temp,recur(n-i,size)+nums[n-1])
                # print(temp,n)
            dp[n]=temp
            return dp[n]
        
        recur(n,size)
        recur(n-1,size)
        return max(dp[n-1],dp[n])
        