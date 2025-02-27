from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        index_map = {num: i for i, num in enumerate(arr)}  # Store indices of elements
        memo = {}  # Memoization for (prev, prev1) pairs

        def dp(prev, prev1):
            if (prev, prev1) in memo:
                return memo[(prev, prev1)]

            next_val = arr[prev] + arr[prev1]
            if next_val in index_map:
                next_idx = index_map[next_val]
                memo[(prev, prev1)] = 1 + dp(prev1, next_idx)
                return memo[(prev, prev1)]
            else:
                return 2  # Minimum length for a valid sequence is 2

        max_len = 0
        for i in range(n):
            for j in range(i + 1, n):
                max_len = max(max_len, dp(i, j))
        
        return max_len if max_len > 2 else 0  # Return 0 if no valid subsequence exists
