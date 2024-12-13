import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        #simple sort solution(faster than heap)
        # new=[(j,i) for i,j in enumerate(nums)]
        # new.sort()
        # print(new)
        # seen=set()
        # score=0
        # for val,idx in new:
        #     if idx not in seen:
        #         print(val)
        #         score+=val
        #         seen.add(idx-1)
        #         seen.add(idx+1)
        # return score
        
        
        
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

        #monotonic decreasing stack

        stk = []
        res = 0
        for i in range(len(nums)):
            if not stk or nums[i] < stk[-1]:
                stk.append(nums[i])
            else:
                while stk:
                    res += stk.pop()
                    if stk:
                        stk.pop()
        while stk:
            res += stk.pop()
            if stk:
                stk.pop()

        return res


