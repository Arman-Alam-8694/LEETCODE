class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # maxx=1
        # n=len(nums)
        # left=0
        # for right in range(n):
        #     if left!=right:
        #         if nums[right-1]>=nums[right]:
        #             left=right
        #     maxx=max(maxx,right-left+1)
        
        # left=0
        # for right in range(n):
        #     if left!=right:
        #         if nums[right-1]<=nums[right]:
        #             left=right
        #     maxx=max(maxx,right-left+1)

        # return maxx
        maxx=inc_left=dec_left=0
        n=len(nums)
    
        for right in range(n):
         
            if nums[right-1]>nums[right]:
                inc_left=right
            elif nums[right-1]<nums[right]:
                dec_left=right
            else: 
                inc_left=right
                dec_left=right

            maxx=max(maxx,right-dec_left+1,right-inc_left+1)
        
        return maxx
        