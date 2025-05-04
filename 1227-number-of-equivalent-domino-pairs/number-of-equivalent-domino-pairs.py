class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        mapp={}
        res=0
        for x,y in dominoes:
            if (x,y) in mapp:
                res+=mapp[(x,y)]
                mapp[(x,y)]+=1
            elif (y,x) in mapp:
                res+=mapp[(y,x)]
                mapp[(y,x)]+=1
            else:
                mapp[(x,y)]=1
        
        return res
        