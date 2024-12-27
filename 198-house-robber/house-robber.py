class Solution:
    def rob(self, nums: List[int]) -> int:
    
        n=len(nums)
        #O(n) both Space and time complexity
        # dp=[-1]*(n+1)
        # def recur(n):
        #     if n<=0:
        #         return 0
        #     if dp[n]!=-1:
        #         return dp[n]
        #     dp[n]=max(recur(n-1),nums[n-1]+recur(n-2))
        #     return dp[n]
        
        # return recur(n)

        #O(1) space optimised code 
    
        if n==0:
            return 0
        if n==1:
            return nums[0]
        prev2=0
        prev1=nums[0]
        for i in range(1,n):
            cur=max(prev1,prev2+nums[i])
            prev2=prev1
            prev1=cur
        return prev1


        