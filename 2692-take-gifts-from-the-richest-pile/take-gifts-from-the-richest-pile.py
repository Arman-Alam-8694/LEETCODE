import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i]=-1*gifts[i]
        heapq.heapify(gifts)

   
        for _ in range(k):
            item=heapq.heappop(gifts)
            if item==-1:
                heapq.heappush(gifts,-1)
                break
            nitem=(math.floor((-item)**0.5))
            
            heapq.heappush(gifts,-nitem)
           

        summ=0
        for i in gifts:
            summ+=abs(i)
        return summ

        