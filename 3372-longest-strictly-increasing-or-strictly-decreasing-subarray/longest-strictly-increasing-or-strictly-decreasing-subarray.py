class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing=1
        decreasing=1
        n=len(nums)
        left=0
        for right in range(n):
            if left!=right:
                if nums[right-1]>=nums[right]:
                    left=right
            increasing=max(increasing,right-left+1)
        
        left=0
        for right in range(n):
            if left!=right:
                if nums[right-1]<=nums[right]:
                    left=right
            decreasing=max(decreasing,right-left+1)

        return max(increasing,decreasing)
        