class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        heap=[]
        for passs,total in classes:
            answer=((passs+1)/(total+1))-(passs/total)
            heapq.heappush(heap,(-answer,passs,total))
        for _ in range(extraStudents):
            res,pstud,total=heapq.heappop(heap)
            pstud+=1
            total+=1
            answer=((pstud+1)/(total+1))-(pstud/total)
            heapq.heappush(heap,
            (-answer,pstud,total))
        
        result=0
        n=len(classes)
        for cal,passs,total in heap:
            result+=(passs/total)
        return result/n



         