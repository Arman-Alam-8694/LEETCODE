import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        need = k - 1

        left, right = [], []
        dl, dr = defaultdict(int), defaultdict(int)

        sumL = 0
        lsize = rsize = 0

        def prune(h, d, sign):
            while h and d[sign * h[0]] > 0:
                d[sign * h[0]] -= 1
                heapq.heappop(h)

        def rebalance():
            nonlocal sumL, lsize, rsize
            while lsize > need:
                prune(left, dl, -1)
                x = -heapq.heappop(left)
                sumL -= x
                lsize -= 1
                heapq.heappush(right, x)
                rsize += 1

            while lsize < need:
                prune(right, dr, 1)
                if not right:
                    break
                x = heapq.heappop(right)
                sumL += x
                rsize -= 1
                heapq.heappush(left, -x)
                lsize += 1

        # initial window
        for i in range(1, dist + 2):
            heapq.heappush(left, -nums[i])
            sumL += nums[i]
            lsize += 1

        rebalance()
        ans = sumL

        for i in range(dist + 2, len(nums)):
            out = nums[i - dist - 1]

            if out <= -left[0]:
                dl[out] += 1
                sumL -= out
                lsize -= 1
            else:
                dr[out] += 1
                rsize -= 1

            x = nums[i]
            if left and x <= -left[0]:
                heapq.heappush(left, -x)
                sumL += x
                lsize += 1
            else:
                heapq.heappush(right, x)
                rsize += 1

            prune(left, dl, -1)
            prune(right, dr, 1)
            rebalance()

            ans = min(ans, sumL)

        return nums[0] + ans
