class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        def ceill(nums):
            ans=nums/3
            if int(ans)==ans:
                return int(ans)
            else:
                return int(ans)+1
        heap=[]
        score=0
        n=len(nums)
        for i in range(n):
            heap.append([-nums[i],i])
        heapq.heapify(heap)
        for i in range(k):
            val,idx=heapq.heappop(heap)
            score+=abs(val)
            assign=ceill(abs(val))
            # print(assign,score)
            heapq.heappush(heap,[assign*-1,idx])
        return score



        
        