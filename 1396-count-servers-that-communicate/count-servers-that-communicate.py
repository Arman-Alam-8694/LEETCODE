class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        temp_col={(0,i):(0,"n") for i in range(col)}
        # visited=set()
        result=0
        for i in range(row):
            found=False
            temp=[]
            for j in range(col):
                if grid[i][j]==1:
                    if not found:
                        temp.append((i,j))
                    if not found and temp_col[(0,j)][0]==0:
                        temp_col[(0,j)]=(1,"n")
                    if found:
                        result+=1
                        temp_col[(0,j)]=(1,"v")
                        grid[i][j]=-1
                        # visited.add((i,j))
                if len(temp)==2:
                 
                    result+=2
                    found=True
                    for x,y in temp:
                        grid[x][y]=-1
                        # visited.add((x,y))
                        temp_col[(0,y)]=(1,"v")
                    temp=[]

        for c in range(col):
            temp=0
            count=0
            if temp_col[(0,c)][1]=="v":
                found=True
            else:
                found=False
            for r in range(row):
                if grid[r][c]==1 :
                    if found:
                        temp+=1
                    if not found:
                        count+=1
                        if count==2:
                            temp+=2
                            found=True
            result+=temp
        return result

        
        