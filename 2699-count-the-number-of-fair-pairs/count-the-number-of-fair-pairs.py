from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0

        def bisect_left(num, start):
            low, high = start, n - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < num:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        def bisect_right(num, start):
            low, high = start, n - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= num:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        for i in range(n):
            low = lower - nums[i]
            high = upper - nums[i]
            left = bisect_left(low, i + 1)
            right = bisect_right(high, i + 1)
            res += right - left

        return res
