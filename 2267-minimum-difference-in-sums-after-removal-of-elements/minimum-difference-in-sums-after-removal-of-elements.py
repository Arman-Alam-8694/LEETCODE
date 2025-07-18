import heapq
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        
        first_half = [0] * (2 * n)
        first_sum = 0
        first = []
        
        for i in range(2 * n):
            heapq.heappush(first, -nums[i])  # max-heap via negation
            first_sum += nums[i]
            if len(first) > n:
                first_sum += heapq.heappop(first)  # remove largest (smallest negative)
            if len(first) == n:
                first_half[i] = first_sum
        
        second_half = [0] * (2 * n)
        second_sum = 0
        second = []
        
        for i in range(3 * n - 1, n - 1, -1):
            heapq.heappush(second, nums[i])  # min-heap for largest n numbers
            second_sum += nums[i]
            if len(second) > n:
                second_sum -= heapq.heappop(second)  # remove smallest
            if len(second) == n:
                second_half[(i - n)] = second_sum  # natural left-to-right indexing

        res = float('inf')
        for i in range(n - 1, 2 * n):
            res = min(res, first_half[i] - second_half[i - (n - 1)])
        
        return res
