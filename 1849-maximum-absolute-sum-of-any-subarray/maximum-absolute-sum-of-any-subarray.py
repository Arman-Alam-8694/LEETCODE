from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0  # Tracks the maximum subarray sum
        min_sum = 0  # Tracks the minimum subarray sum
        curr_max = 0  # Running maximum sum
        curr_min = 0  # Running minimum sum

        for num in nums:
            # Kadane's for maximum sum subarray
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)
            
            # Kadane's for minimum sum subarray
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)
        
        # Return the max absolute sum
        return max(abs(max_sum), abs(min_sum))
