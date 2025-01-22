from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row=len(isWater)
        col=len(isWater[0])
        result=[[-1]*col for _ in range(row)]
        visited=set()
    
        listt=[]
        for r in range(row):
            for c in range(col):
                if isWater[r][c]==1:
                    listt.append((0,r,c))
                    result[r][c]=0
                          
        queue=deque(listt)
        dir=[(0,1),(1,0),(-1,0),(0,-1)]
        while queue:
            max_h,i,j=queue.popleft()
            for x,y in dir:
                a=x+i
                b=y+j
                if 0<=a<row and 0<=b<col and result[a][b]==-1:
                    queue.append((max_h+1,a,b))
                    result[a][b]=max_h+1

        return result
