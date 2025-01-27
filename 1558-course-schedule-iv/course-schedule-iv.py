class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        rpath=[0]*n
        adj=[[] for _ in range(n)]
        deg=[0]*n
        for a, b in prerequisites:
            adj[a].append(b)
            rpath[b]|=(1<<a)
            deg[b]+=1
        
        q=deque()
        for i in range(n):
            if deg[i]==0: q.append(i)
        
        while q:
            i=q.popleft()
            for j in adj[i]:
                rpath[j]|=rpath[i]
                deg[j]-=1
                if deg[j]==0:
                    q.append(j)
        ans=[False]*len(queries)
        for i, (q0, q1) in enumerate(queries):
            ans[i]=(rpath[q1]>>q0)&1==1
        return ans
        