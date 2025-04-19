class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0  
        for i, num in enumerate(nums): 
            # lower - nums[j] <= nums[i] <= upper - nums[j]
            res += bisect_right(nums, upper - num, 0, i) - bisect_left(nums, lower - num, 0, i) 
        
        return res 