class Solution:
    def numTilings(self, n: int) -> int:
        MOD=10**9+7
        @cache
        def recur(x,y):
            if x>n or y>n:
                return 0
            if x==n and y==n:
                return 1
            
            if x==y:
                ways=(
                    recur(x+1,y+1)+
                    recur(x+2,y+2)+
                    recur(x+2,y+1)+
                    recur(x+1,y+2)

                )
          
            elif x>y:
                ways=(
                    recur(x,y+2)+
                    recur(x+1,y+2)
                )
            
            else:
                ways=(
                    recur(x+2,y)+
                    recur(x+2,y+1)
                )
            return (ways)%MOD
    
        return recur(0,0)