class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap=[-i for i in nums]
        score=0
        heapq.heapify(heap)
        for _ in range(k):
            score-=heapq.heappushpop(heap,heap[0]//3)
        return score



        
        