class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap=[-i for i in nums]
        score=0
        n=len(nums)

        heapq.heapify(heap)
        for i in range(k):
            val=heapq.heappop(heap)
            val=abs(val)
            score+=val
            assign=math.ceil(val/3)
            # print(assign,score)
            heapq.heappush(heap,-assign)
        return score



        
        