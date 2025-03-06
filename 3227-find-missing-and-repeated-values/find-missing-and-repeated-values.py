class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        mapp={}
        result=[0,0]
        m=len(grid)
        sett=set([i for i in range(1,m*m+1)])
        # print(sett)
        for i in range(m):
            for j in range(m):
                curr=grid[i][j]
                sett.discard(curr)
                mapp[curr]=mapp.get(curr,0)+1
                if mapp[curr]==2:
                    result[0]=curr
        result[1]=next(iter(sett))
        return result
                


        