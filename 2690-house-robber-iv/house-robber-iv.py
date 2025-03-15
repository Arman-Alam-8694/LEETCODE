from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = min(nums), max(nums)  # Binary search range
        res = right
        
        def canRobWithCapability(cap):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:  # Can rob this house
                    count += 1
                    i += 1  # Skip adjacent house
                i += 1  # Move to next house
                
                if count >= k:  # Successfully picked k houses
                    return True
            return False

        while left <= right:
            mid = (left + right) // 2
            if canRobWithCapability(mid):
                res = mid  # Try to minimize capability
                right = mid - 1
            else:
                left = mid + 1

        return res
