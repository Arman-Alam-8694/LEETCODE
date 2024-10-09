class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def ispossible(days):
            flowers=0
            bouquets=0
            for i in bloomDay:
                if i<=days:
                    flowers+=1
                else:
                    flowers=0
                if flowers%k==0:
                    bouquets+=flowers//k
                    flowers=0
            return bouquets>=m


            
        n=len(bloomDay)
        if n<(m*k):
            return -1
        left=min(bloomDay)
        right=max(bloomDay)
        while left<=right:
            mid=(left+right)//2
            if ispossible(mid):
                right=mid-1
            else:
                left=mid+1
        return left
        