class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        store=[[0,0]  for i in range(col)]
        res=0

        def check(curr):
            if curr=="X":
                return 0
            elif curr=="Y":
                return 1
            else:
                return -1
        for i in range(row):
            rsum=[0,0]
            for j in range(col):
               
                temp=check(grid[i][j])
                if temp!=-1:
                    store[j][temp]=(store[j][temp]+1)
                rsum[0]+=store[j][0]
                rsum[1]+=store[j][1]
                if rsum[0]==rsum[1] and rsum[0]>=1:
                    res+=1

                        
        return res
        