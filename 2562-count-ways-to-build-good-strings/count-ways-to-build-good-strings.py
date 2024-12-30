class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD=10**9+7
        dp=[0]*high
        ways=0
        @cache
        def recur(low,high,size,ways):
            if size>high:
                return 0
            ways=0
            if low<=size<=high:
                ways+=1
            ways+=recur(low,high,size+one,ways)
            ways+=recur(low,high,size+zero,ways)
            return ways%MOD
        return recur(low,high,0,ways)

        
        