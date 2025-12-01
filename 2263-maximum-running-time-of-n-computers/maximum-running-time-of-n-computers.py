import heapq

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        right=sum(batteries)
        left=min(batteries)
        batteries.sort()
        total=sum(batteries[:-n])
       
        answer=float("inf")


        def tryy(limit):
            cur=0
        
            for i in range(-n,0):

                if limit<batteries[i]:
                    continue
                cur+=(limit-batteries[i])
           
            return cur<=total

        while left<=right:
            mid=(left+right)//2
            if tryy(mid):
                answer=mid
                left=mid+1
            else:
                right=mid-1
      
        return answer if answer!=float("inf") else 0

