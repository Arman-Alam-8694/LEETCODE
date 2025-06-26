class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left,right=0,max(bloomDay)

        def possible(days):
            flowers=0
            pots=0
            for i in bloomDay:
                if i<=days:
                    flowers+=1
                    if flowers==k:
                        pots+=1
                        flowers=0
                else:
                    flowers=0
            # print(pots,days)
            return pots>=m


        if m*k>len(bloomDay):
            return -1
        answer=-1
        while left<=right:
            mid=(left+right)//2
            if possible(mid):
                answer=mid
                right=mid-1
            else:
                left=mid+1
        return answer
        
        