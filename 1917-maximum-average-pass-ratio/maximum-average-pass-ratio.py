class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def calc(passs,total):
            answer=((passs+1)/(total+1))-(passs/total)
            return (-answer,passs,total)
        heap=[]
        for pstud,total in classes:
            heapq.heappush(heap,calc(pstud,total))
        for _ in range(extraStudents):
            res,pstud,total=heapq.heappop(heap)
            pstud+=1
            total+=1
            heapq.heappush(heap,
            calc(pstud,total))
        
        result=0
        n=len(classes)
        while heap:
            cal,passs,total=heapq.heappop(heap)
            result+=(passs/total)

      
        return result/n



         