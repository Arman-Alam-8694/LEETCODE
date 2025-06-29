from typing import List
import bisect

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        # Precompute powers of 2 mod MOD
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i-1] * 2) % MOD

        result = 0

        # For each left as the min element...
        for left in range(n):
            # Find the largest right such that nums[left] + nums[right] <= target
            # bisect_right returns the insertion point > (target - nums[left])
            # so we subtract 1 to get the last valid index
            right = bisect.bisect_right(nums, target - nums[left], lo=left) - 1

            if right >= left:
                # All subsequences with this fixed min (at `left`) and max (anywhere up to `right`)
                # count = 2^(right-left) (choose to include or not include each of the right-left middle elements)
                result = (result + pow2[right - left]) % MOD

        return result
