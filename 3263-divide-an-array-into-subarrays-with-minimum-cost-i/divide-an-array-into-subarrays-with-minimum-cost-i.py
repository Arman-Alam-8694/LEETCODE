class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first,second=float("inf"),float("inf")
        for i in range(1,len(nums)):
            if nums[i]<first:
                second=first
                first=nums[i]
            elif nums[i]<second:
                second=nums[i]
        return nums[0]+first+second


        
        