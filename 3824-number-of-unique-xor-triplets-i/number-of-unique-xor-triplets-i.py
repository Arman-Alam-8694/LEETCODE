class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2:
            return n
        m = 1
        while (m << 1) <= n:
            m <<= 1
        return 2 * m
