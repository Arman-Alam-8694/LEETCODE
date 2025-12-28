class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # return sum([1 for j in grid for i in j if i<0 ])
        row=len(grid)
        col=len(grid[0])
        cur=col-1
        pos=0
        for i in range(row):
            while cur!=-1:
                if grid[i][cur]>=0:
                    pos+=cur+1
                    break
                else:
                    cur-=1
            if cur==-1:
                break
        return (row*col)-pos
            
                
    


            
        