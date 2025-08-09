class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        temp=2
        if n==1:
            return True
        else:
            while temp<n:
                temp*=2
            return temp==n

        