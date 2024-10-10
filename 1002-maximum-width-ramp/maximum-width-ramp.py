class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        indices=[i for i in range(len(nums))]
        indices.sort(key=lambda i:(nums[i],i))
        min_index=len(nums)
        max_width=0
        for idx in indices:
            max_width=max(max_width,idx-min_index)
            min_index=min(min_index,idx)

        
        
        return max_width
