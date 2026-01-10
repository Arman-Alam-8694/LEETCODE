class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n=len(s1)
        m=len(s2)

        @cache
        def dp(x,y):
            if x==n:
                return sum(map(ord,s2[y:]))
            if y==m:
                return sum(map(ord,s1[x:]))
            if s1[x]==s2[y]:
                return dp(x+1,y+1)
           
            first=ord(s1[x])+dp(x+1,y)
            second=ord(s2[y])+dp(x,y+1)
            return min(first,second)
        return dp(0,0)

            
            
    
        