class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        seen=set()
        row=len(moveTime)
        col=len(moveTime[0])
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        heap=[(0,0,0)]
        while heap:
            time,x,y=heapq.heappop(heap)
            if x==row-1 and y==col-1:
                return time
            # seen.add((x,y))
            for dx,dy in direction:
                nx=x+dx
                ny=y+dy
                if (nx,ny) not in seen and 0<=nx<row and 0<=ny<col:
                    seen.add((nx,ny))
                    if time<=moveTime[nx][ny]:
                        heapq.heappush(heap,(moveTime[nx][ny]+1,nx,ny))
                    else:
                        heapq.heappush(heap,(time+1,nx,ny))
                    

        