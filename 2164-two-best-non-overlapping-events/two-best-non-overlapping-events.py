class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        heap=[]
        # heapq.heapify(heap)
        # while heap:
        #     h=heapq.heappop(heap)
        #     print(h)
        # return 0
        events.sort(key=lambda x:(x[0],x[1]))
        n=len(events)
        best=0
        maxx=0
        maxx_end=float(inf)
        for s,e,v in events:
        
            
            while heap and heap[0][0]<s:
                te,ts,tv=heapq.heappop(heap)
                best=max(best,v+tv)
                
                if tv>maxx:
                    maxx=tv
                    maxx_end=te
                elif tv==maxx and te<maxx_end:
                    maxx_end=te

            heapq.heappush(heap,(e,s,v))
            best=max(best,v)
            if maxx_end<s:
                best=max(best,v+maxx)
        
        return best



        