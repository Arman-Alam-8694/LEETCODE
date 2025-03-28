class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        def calculate(k,last,queue):
            directions=[(0,1),(1,0),(-1,0),(0,-1)]
            m=len(grid)
            n=len(grid[0])
            prev=0
            invalid=deque([])
            if k==6:
                print(queue)
                print(last)
            while queue:    
                x,y=queue.popleft()
                if grid[x][y]<k and grid[x][y]!=-1 :
                    # if k==6:
                        # print(grid[x][y])
                    grid[x][y]=-1
                    last+=1
                    for dx,dy in directions:
                        if 0<=dx+x<m and 0<=dy+y<n and grid[dx+x][dy+y]!=-1:
                            queue.append((dx+x,dy+y))
                else:
                    if grid[x][y]!=-1:
                        invalid.append((x,y))

            return last,invalid
            
                    

        original=queries[:]
        queries.sort()
        queue=deque()
        queue.append((0,0))
        last_point=0
        prev=-1
        mapp=defaultdict(int)
        for i in queries:
            if i in mapp:
                print("here")
                continue
            ans,queue=calculate(i,last_point,queue)
            last_point=ans
            mapp[i]=last_point
        
        res=[]
        for i in original:
            res.append(mapp[i])


        return res