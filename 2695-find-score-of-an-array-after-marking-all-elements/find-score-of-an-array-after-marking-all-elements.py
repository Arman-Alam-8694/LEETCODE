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

        #simple pointer
        score=0
        skip=False
        prev=None
        # 18 9 7 6 1 3 4 5
        stack=[]
        for i in range(len(nums)):
            if skip==True:
                continue
            if not prev and nums[i]<=nums[i+1]:
                score+=nums[i]
                skip=True
            elif prev and nums[i]<=nums[i+1]:
                score+=nums[i]
                skip=True
                if not prev and stack:
                    stack.pop()

            elif nums[i]>nums[i+1]:
                stack.append(nums[i])
                prev=True
        skip=False
        while stack:
            if not skip:
                score+=stack.pop()
                skip=True
            if skip:
                stack.pop()
                skip=False
        return score



