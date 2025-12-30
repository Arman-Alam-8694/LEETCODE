class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        x=0
        y=0
        ans=0
        def check_row(x,y):
            temp=-1
            tmin=float("inf")
            tsum=-1
            count=set()
            for i in range(3):
                ttsum=0
                for j in range(3):
                    temp=max(temp,grid[x+i][y+j])
                    tmin=min(tmin,grid[x+i][y+j])
                    ttsum+=grid[x+i][y+j]
                    count.add(grid[x+i][y+j])

                    if temp>9:
                        break
                    if tmin<1:
                        break
                if temp>9:
                    return False,tsum
                if tmin<1:
                    return False,tsum
                if (i+1)*3!=len(count):
                    return False,tsum
                if tsum==-1:
                    tsum=ttsum
                elif tsum!=ttsum:
                    return False,tsum
            return True,tsum
        def check_col(x,y):
            
            tsum=-1
           
            for i in range(3):
                ttsum=0
                for j in range(3):
                   
                    ttsum+=grid[x+j][y+i]
                   

                   
              
                if tsum==-1:
                    tsum=ttsum
                elif tsum!=ttsum:
                    return False,tsum
            return True,tsum


        def check_d(x,y):
            first=0
            for i in range(3):
                a=grid[x+i][y+i]
                first+=a
            second=0
                
            for i in range(3):
                a=grid[x+i][y+2-i]
                second+=a
            if first==second:
                return True,first
            else:
                return False,first


        for x in range(row-2):
            for y in range(col-2):
                pos,val=check_row(x,y)
                if pos:
                    cpos,cval=check_col(x,y)
                    if cpos and cval==val:
                        dpos,dval=check_d(x,y)
                        if dpos and dval==cval:
                            ans+=1
        return ans


        