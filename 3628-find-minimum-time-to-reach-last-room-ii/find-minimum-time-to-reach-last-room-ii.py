class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        seen=set()
        row=len(moveTime)
        col=len(moveTime[0])
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        heap=[(0,0,0,1)]
        seen.add((0,0))
        prev=(-1,-1)
        counter=1

        while heap:
            time,x,y,counter=heapq.heappop(heap)
            if x==row-1 and y==col-1:
                return time
            # print(x,y,time,counter)
            # if (x,y) in seen:
            #     continue
            # seen.add((x,y))
            for dx,dy in direction:
                nx=x+dx
                ny=y+dy
                if (nx,ny) not in seen and 0<=nx<row and 0<=ny<col:
                    seen.add((nx,ny))
                    if counter==2:
                            heapq.heappush(heap,(max(time+counter,moveTime[nx][ny]+counter),nx,ny,counter-1))
                    else:
                        heapq.heappush(heap,(max(time+counter,moveTime[nx][ny]+counter),nx,ny,counter+1))
                        

                    # else:
                    #     heapq.heappush(heap,(max(time+1,moveTime[nx][ny]+1),nx,ny,1))
    
            # prev=(x,y)

        # 0 0 0 0
        # 0 0 0 0

                    
                    
                    
                   
        # 0 4 
        # 4 4
        # 3
        

        # 22
        # 3,3
        # 12 21 32 23
        # 02 20 42 24
        23 



    
                    
                    

        