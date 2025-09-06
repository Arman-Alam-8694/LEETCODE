from typing import List
import math

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # helper: prefix sum of steps up to n
        def prefix_steps(n: int) -> int:
            if n == 0:
                return 0
            total = 0
            i = 0
            while True:
                left = 4**i
                right = 4**(i+1) - 1
                if left > n:
                    break
                start = left
                end = min(n, right)
                count = end - start + 1
                total += count * (i + 1)  # each in this bucket has (i+1) steps
                i += 1
            return total

        ans = 0
        for l, r in queries:
            total_steps = prefix_steps(r) - prefix_steps(l - 1)
            ans += (total_steps + 1) // 2   # ceil division
        return ans
