from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        # Precompute powers of 2
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        result = 0
        left, right = 0, n - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                # All combinations between left and right are valid
                result = (result + pow2[right - left]) % MOD
                left += 1
            else:
                right -= 1

        return result
