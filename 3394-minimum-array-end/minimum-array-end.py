class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result=x
        n-=1
        mask=1
        while n>0:
            if not (x&mask):
                result|=(n&1)*mask
                n>>=1
            mask<<=1
        return result


        