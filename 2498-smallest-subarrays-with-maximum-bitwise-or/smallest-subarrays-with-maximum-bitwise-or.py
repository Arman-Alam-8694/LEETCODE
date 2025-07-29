from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 1) Turn each number into a binary string (without '0b') 
        #    and find the max length
        bins = [bin(x)[2:] for x in nums]
        max_len = max(len(b) for b in bins)
        # 2) Left‑pad every binary string to the same length with '0'
        bins = [b.zfill(max_len) for b in bins]

        # 3) Build suffix‑OR as strings of '0'/'1'
        suffix_or = [''] * n
        suffix_or[-1] = bins[-1]
        for i in range(n - 2, -1, -1):
            a, b = suffix_or[i + 1], bins[i]
            # OR them character by character
            merged = []
            for ca, cb in zip(a, b):
                # if either bit is '1', result is '1'
                merged.append('1' if ca == '1' or cb == '1' else '0')
            suffix_or[i] = ''.join(merged)

        # 4) Sliding window [L..R] + per‑bit counts
        bit_count = [0] * max_len
        answer = [0] * n
        L = 0

        def covers(target: str) -> bool:
            # For every position where target has '1', we need count>0
            for pos, ch in enumerate(target):
                if ch == '1' and bit_count[pos] == 0:
                    return False
            return True

        # 5) Expand R, then shrink L while still covering suffix_or[L]
        for R in range(n):
            # add bins[R]
            for pos, ch in enumerate(bins[R]):
                if ch == '1':
                    bit_count[pos] += 1

            # try to shrink from L
            while L <= R and covers(suffix_or[L]):
                answer[L] = R - L + 1
                # remove bins[L]
                for pos, ch in enumerate(bins[L]):
                    if ch == '1':
                        bit_count[pos] -= 1
                L += 1

        return answer
