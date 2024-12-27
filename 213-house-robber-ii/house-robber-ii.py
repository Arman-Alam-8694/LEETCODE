class Solution:
    def rob(self, nums: List[int]) -> int:
        
       
        n1=len(nums)
        if n1==1:
            return nums[0]
        arr1=nums[:-1]
        arr2=nums[1:]
        n1-=1

        dp2=[-1]*(n1+1)
        dp1=[-1]*(n1+1)
        def recur(n,dp,arr):
            if n<=0:
                return 0
            if dp[n]!=-1:
                return dp[n]
            dp[n]=max(recur(n-1,dp,arr),arr[n-1]+recur(n-2,dp,arr))
            return dp[n]

        
        return max( recur(n1,dp1,arr1), recur(n1,dp2,arr2))


        
        