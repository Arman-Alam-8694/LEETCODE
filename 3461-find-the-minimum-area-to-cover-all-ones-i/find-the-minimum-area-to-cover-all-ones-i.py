class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rowleft=float("inf")
        rowright=0
        columnleft=float("inf")
        columnright=0
        n=len(grid)
        found=False
        m=len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    found=True
                    rowleft=min(rowleft,j)
                    rowright=max(rowright,j)
                    columnleft=min(columnleft,i)
                    columnright=max(columnright,i)
        
        if found:
            length=rowright-rowleft+1
            breadth=columnright-columnleft+1
            return length*breadth
        return 0
                    


        