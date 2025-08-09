class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and ((n-1)&n==0)
        