# from collections import defaultdict,Counter
# from typing import List



class Solution:
    def maxFrequency(self, A: List[int], k: int) -> int:
        count = Counter(A)
        def kadane(b):
            res = cur = 0
            for a in A:
                if a == k:
                    cur -= 1
                if a == b:
                    cur += 1
                if cur < 0:
                    cur = 0
                res = max(res, cur)
            return res
        res = max(kadane(b) for b in count)
        return count[k] + res