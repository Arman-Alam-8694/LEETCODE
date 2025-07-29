from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 1) compute suffix OR for each index
        suffix_or = [0] * n
        suffix_or[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_or[i] = suffix_or[i + 1] | nums[i]
        
        # 2) sliding window with per‐bit counts
        bit_count = [0] * 32
        answer = [0] * n
        L = 0
        
        def covers(target_or: int) -> bool:
            """Return True if current window's OR covers all bits in target_or."""
            # For each bit set in target_or, bit_count[b] must be > 0
            mask = target_or
            while mask:
                b = (mask & -mask).bit_length() - 1
                if bit_count[b] == 0:
                    return False
                mask &= mask - 1
            return True
        
        for R in range(n):
            # add nums[R] into window
            x = nums[R]
            for b in range(32):
                if x & (1 << b):
                    bit_count[b] += 1
            
            # now shrink from the left as far as we still cover suffix_or[L]
            while L <= R and covers(suffix_or[L]):
                answer[L] = R - L + 1
                # remove nums[L] and advance L
                y = nums[L]
                for b in range(32):
                    if y & (1 << b):
                        bit_count[b] -= 1
                L += 1
        
        return answer
