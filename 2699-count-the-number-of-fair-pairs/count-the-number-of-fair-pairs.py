from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        result = 0
        n = len(nums)

        def bisect_left(num):
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def bisect_right(num):
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= num:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        for i in range(n):
            low = lower - nums[i]
            high = upper - nums[i]
            l = bisect_left(low)
            r = bisect_right(high)
            result += r - l

            # Exclude self-pairing (i == j)
            if low <= nums[i] <= high:
                result -= 1

        return result // 2  # each pair counted twice
