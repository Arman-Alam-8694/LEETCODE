from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)

        @cache
        def subset(i, curr_sum):
            if curr_sum == target:
                return True
            if curr_sum > target or i >= n:
                return False
            # include nums[i] or skip it
            return subset(i + 1, curr_sum + nums[i]) or subset(i + 1, curr_sum)

        return subset(0, 0)
