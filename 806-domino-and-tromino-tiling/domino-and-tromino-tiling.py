class Solution:
    def numTilings(self, n: int) -> int:
        #RECURSIVE 
        # MOD=10**9+7
        # @cache
        # def recur(x,y):
        #     if x>n or y>n:
        #         return 0
        #     if x==n and y==n:
        #         return 1
            
        #     if x==y:
                  #@
                  #@
        #         ways=(
        #             recur(x+1,y+1)+
        #             recur(x+2,y+2)+
        #             recur(x+2,y+1)+
        #             recur(x+1,y+2)

        #         )
          
        #     elif x>y:
                #@@
                #@
        #         ways=(
        #             recur(x,y+2)+
        #             recur(x+1,y+2)
        #         )
            
        #     else:
                #@
                #@@
        #         ways=(
        #             recur(x+2,y)+    
        #             recur(x+2,y+1)
        #         )
        #     return (ways)%MOD
    
        # return recur(0,0)


        dp=[0]*(n+4)
        MOD=10**9+7
        dp[0]=1
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=(2*dp[i-1]+dp[i-3])%MOD
        return dp[n]