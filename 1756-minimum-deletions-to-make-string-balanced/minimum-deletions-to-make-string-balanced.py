class Solution:
    def minimumDeletions(self, s: str) -> int:

        store=[[None,None] for i in range(len(s))]
        def recurse(i,found):
            if i==len(s):
                return 0
         
            if found:
                if store[i][1]!=None:
                    return store[i][1]
            else:
                if store[i][0]!=None:
                    return store[i][0]
            res=1+recurse(i+1,found)
            if s[i]=="a":
            
                if not found:
                    res=min(res,recurse(i+1,False))
            else:
                res=min(res,recurse(i+1,True))

          
            if found:
                store[i][1]=res
            else:
                store[i][0]=res
            return res
            
        return recurse(0,False)