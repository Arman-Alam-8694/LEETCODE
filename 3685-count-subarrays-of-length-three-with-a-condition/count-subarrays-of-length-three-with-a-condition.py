class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        result=0
        for right in range(2,len(nums)):
            if (nums[right]+nums[right-2])*2==(nums[right-1]):
                result+=1
        return result
        