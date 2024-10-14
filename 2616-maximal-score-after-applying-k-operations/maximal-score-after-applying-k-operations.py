class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap=[]
        score=0
        n=len(nums)
        for i in range(n):
            heap.append([-nums[i],i])
        heapq.heapify(heap)
        for i in range(k):
            val,idx=heapq.heappop(heap)
            score+=abs(val)
            assign=math.ceil(abs(val)/3)
            # print(assign,score)
            heapq.heappush(heap,[assign*-1,idx])
        return score



        
        