import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        #simple sort solution(faster than heap)
        new=[(j,i) for i,j in enumerate(nums)]
        new.sort()
        seen=set()
        score=0
        for val,idx in new:
            if idx not in seen:
                score+=val
                seen.add(idx-1)
                seen.add(idx+1)
        return score
        
        
        
        #heap solution(slower)
        
        # new=[(j,i) for i,j in enumerate(nums)]
        # heapq.heapify(new)
        # score=0
        # seen=set()
        # while new:
        #     val,idx=heapq.heappop(new)
        #     if idx not in seen:
        #         score+=val
        #         seen.add(idx-1)
        #         seen.add(idx+1)
        # return score



