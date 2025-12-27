class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms=[0]*n
        meetings.sort(key=lambda x:x[0])
        heap=[i for i in range(n)]
        heapq.heapify(heap)
        current=[]
        cur_time=0
        for start,end in meetings:
            cur_time=max(cur_time,start)
            while current and cur_time>=current[0][0]:
                tend,rm,tstart=heapq.heappop(current)
                heapq.heappush(heap,rm)
            if heap:
                rm=heapq.heappop(heap)
                heapq.heappush(current,(cur_time+(end-start),rm,cur_time))
                rooms[rm]+=1
            
            else:
                while current and (not heap):
                    cur_time=current[0][0]
                    while current and cur_time>=current[0][0]:
                        tend,rm,tstart=heapq.heappop(current)
                        heapq.heappush(heap,rm)
                if heap:
                    rm=heapq.heappop(heap)
                    heapq.heappush(current,(cur_time+(end-start),rm,cur_time))
                   
                    rooms[rm]+=1
        
        return rooms.index(max(rooms))


        