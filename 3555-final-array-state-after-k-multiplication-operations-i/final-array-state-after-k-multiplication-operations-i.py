import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap=[(num,idx) for idx,num in enumerate(nums)]
        heapq.heapify(heap)
        for _ in range(k):
            item,idx=heapq.heappop(heap)
            nums[idx]=item*multiplier
            heapq.heappush(heap,(item*multiplier,idx))

        # print(heap)
        # for val,idx in heap:
        #     nums[idx]=val
        return nums
        