# class Solution:
#     def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
#         n=len(cells)
#         grid=[[0]*col for i in range(row)]
#         parent=list(range(n+2))
#         top,bottom=n,n+1
#         size=[1]*(n+2)
#         def index(x,y):
#             return x*col+y
#         def find(x):
#             if parent[x]!=x:
#                 parent[x]=find(parent[x])
#             return parent[x]
#         def dsu(left,right):
#             l=find(left)
#             r=find(right)
#             if l==r:
#                 return
#             if size[l]>size[r]:
#                 parent[l]=r
#             else:
#                 parent[r]=l
            
#         dirr=[(0,1),(1,0),(0,-1),(-1,0)]
#         for day in range(n-1,-1,-1):
#             r,c=cells[day]
#             r-=1
#             c-=1
#             grid[r][c]=1
#             curr=index(r,c)
#             for x,y in dirr:
#                 nx=x+r
#                 ny=y+c
#                 if 0<=nx<row and 0<=ny<col:
#                     if grid[nx][ny]==1:
#                         dsu(index(nx,ny),curr)
            
#             if r==0:
#                 dsu(top,curr)
#             if r==row-1:
#                 dsu(bottom,curr)
#             if find(top)==find(bottom):
#                 return day

        



class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def possible(day):
            grid=[[0]*col for i in range(row)]
            for i in range(day):
                r,c=cells[i]
                r-=1
                c-=1
                grid[r][c]=1
            visited=[[0]*col for i in range(row)]
            dir=[(0,1),(0,-1),(1,0),(-1,0)]
            def dfs(x,y):
                visited[x][y]=1
                if x==row-1:
                    return True
                for dx,dy in dir:
                    nx=dx+x
                    ny=dy+y
                    if 0<=nx<row and 0<=ny<col:
                        if not visited[nx][ny] and grid[nx][ny]==0:
                            if dfs(nx,ny):
                                return True
                return False

            for k in range(col):
                if grid[0][k]==0:
                    if dfs(0,k):
                        return True
            return False
                



        left,right=1,len(cells)
        ans=0
        while left<=right:
            mid=(left+right)//2
            if possible(mid):
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans