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
            nitem=int((-item)**0.5)
            
            heapq.heappush(gifts,-nitem)
           

        return -sum(gifts)
        