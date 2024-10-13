class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        start=float("inf")
        end=float("inf")
        rangee=[start,end]
        k=len(nums)
        min_dif=float("inf")
        heap=[(nums[i][0],0,i) for i in range(k)]
        maxx=max(heap)[0]
        heapq.heapify(heap)
        while len(heap)==k:
            minn,eidx,lidx=heapq.heappop(heap)
            if maxx-minn<min_dif:
                rangee=[minn,maxx]
                start=minn
                end=maxx
                min_dif=maxx-minn
            if len(nums[lidx])==eidx+1:
                return rangee
            heapq.heappush(heap,(nums[lidx][eidx+1],eidx+1,lidx))
            new=nums[lidx][eidx+1]
            if new>maxx:
                maxx=new
        return rangee





        