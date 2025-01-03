class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n=len(nums)
        prefsum=[0]*(n+1)
        cnt=0
        for i in range(n):
            cnt+=nums[i]
            prefsum[i]=cnt
        result=0
        for i in range(n-1):
            if prefsum[i]>=(prefsum[n-1]-prefsum[i]):
                result+=1
        return result
        
        

        