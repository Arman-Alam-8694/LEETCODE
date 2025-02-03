class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxx=1
        n=len(nums)
        left=0
        for right in range(n):
            if left!=right:
                if nums[right-1]>=nums[right]:
                    left=right
            maxx=max(maxx,right-left+1)
        
        left=0
        for right in range(n):
            if left!=right:
                if nums[right-1]<=nums[right]:
                    left=right
            maxx=max(maxx,right-left+1)

        return maxx
        