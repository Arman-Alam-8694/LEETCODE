class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp=Counter(nums)
        stack=[]
        for key,v in mapp.items():
            heapq.heappush(stack,(v,key))
            if len(stack)>k:
                heapq.heappop(stack)
        return [key for v,key in stack]

        