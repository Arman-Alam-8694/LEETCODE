from collections import deque 
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def check(start,mappp,graph):
            queue=deque([start])
            mapp[start]=0
            

            while queue:
                node=queue.popleft()
                for son in graph[node]:
                    if son not in mapp:
                        queue.append(son)
                        mapp[son]=1-mapp[node]
                    else:
                        if mapp[node]==mapp[son]:
                            return False
            
            return True
       
        mapp={}
        for i in range(len(graph)):
            if i not in mapp:
                if not check(i,mapp,graph):
                    return False

        return True
        