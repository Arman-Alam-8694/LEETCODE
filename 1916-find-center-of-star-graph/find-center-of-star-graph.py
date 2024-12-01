class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        mapp={}
        maxx=-1
        for u,v in edges:
            mapp[u]=mapp.get(u,0)+1
            mapp[v]=mapp.get(v,0)+1
            if mapp[u]>maxx:
                maxx=u
            if mapp[v]>maxx:
                maxx=v
        return maxx
        

            
        