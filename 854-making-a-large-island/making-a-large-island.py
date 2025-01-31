class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        dir=[(1,0),(0,1),(-1,0),(0,-1)]
        col=len(grid[0])
     
        summ = sum(sum(row) for row in grid)
        if summ==row*col:
            return row*col
        elif summ==0:
            return 1
        components=[]
        visited=set()

        def bfs(stack,visited):
            i,j,cur_size=stack[0]
            temp=[]
            temp.append((i,j))
            maxx=cur_size
            while stack:
                i,j,cur_size=stack.popleft()
                for x,y in dir:
                    a=i+x
                    b=j+y
                    if 0<=a<row and 0<=b<col and (a,b) not in visited:
                        if grid[a][b]==1:
                            cur_size+=1
                            maxx=max(maxx,cur_size)
                            temp.append((a,b))
                            stack.appendleft((a,b,cur_size))
                            visited.add((a,b))

            t=temp[:]
            components.append([t,len(t)])

           
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and (i,j) not in visited:
                    stack=deque([(i,j,1)])
                    visited.add((i,j))
                    bfs(stack,visited)
                visited.add((i,j))


        if not components:
            return row*col
    
        mapp={}
        maxi=0
        for c_list,maxx in components:
            visited=set()
            maxi=max(maxi,maxx)
            for i,j in c_list:
                for x,y in dir:
                    a=i+x
                    b=j+y
                    if 0<=a<row and 0<=b<col and grid[a][b]==0 and (a,b) not in visited:
                        if (a,b) not in mapp:
                            mapp[(a,b)]=maxx+1
                        else:
                            mapp[(a,b)]+=maxx
                        visited.add((a,b))

        return max(mapp.values())
      
        
       