from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        left = 0  # start of a zero segment
        
        for right in range(len(nums)):
            if nums[right] != 0:
                # If we have a zero segment before this non-zero
                n = right - left
                result += (n * (n + 1)) // 2
                left = right + 1  # move left to next potential zero segment
        
        # Handle the case where the array ends with zeros
        if left < len(nums):
            n = len(nums) - left
            result += (n * (n + 1)) // 2
        
        return result
