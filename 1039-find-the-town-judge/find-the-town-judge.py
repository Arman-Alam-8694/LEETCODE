class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mapp={}
        for i in range(1,n+1):
            mapp[i]=[]
        for u,v in trust:
            if u in mapp:
                del mapp[u]
            if v in mapp:
                mapp[v].append(u)
     
        if mapp:
            if len(mapp)>1:
                return -1
            judge=list(mapp.keys())[0]

            if len(mapp[judge])==n-1:
                return judge
            else:
                return -1
        return -1
        