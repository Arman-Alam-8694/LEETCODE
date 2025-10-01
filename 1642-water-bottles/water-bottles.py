class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans=numBottles
        anss=numBottles
        while anss>=numExchange:
            a=anss//numExchange
            ans+=a
            rem=anss%numExchange
            anss=a+rem
        return ans
        