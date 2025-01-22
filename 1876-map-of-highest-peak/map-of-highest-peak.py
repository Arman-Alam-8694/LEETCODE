from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row=len(isWater)
        col=len(isWater[0])
        visited=set()
        # maxx=float("-inf")
        listt=[]
        for r in range(row):
            for c in range(col):
                if isWater[r][c]==1:
                    listt.append((0,r,c))
                    isWater[r][c]=0
                    visited.add((r,c))
                          
        queue=deque(listt)
        dir=[(0,1),(1,0),(-1,0),(0,-1)]
        while queue:
            max_h,i,j=queue.popleft()
            for x,y in dir:
                a=x+i
                b=y+j
                if 0<=a<row and 0<=b<col and (a,b) not in visited and isWater[a][b]==0:
                    queue.append((max_h+1,a,b))
                    isWater[a][b]=max_h+1

        return isWater
