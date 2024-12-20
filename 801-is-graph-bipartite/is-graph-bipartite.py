from collections import deque 
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def check(start,visited,graph,mapp):
            queue=deque([start])
            mapp[start]=0
            

            while queue:
                node=queue.popleft()
                visited.add(node)
                for son in graph[node]:
                    if son not in visited:
                        queue.append(son)
                        mapp[son]=1-mapp[node]
                    else:
                        if mapp[node]==mapp[son]:
                            return False
            
            return True
       
        mapp={}
        visited=set()
        for i in range(len(graph)):
            if i not in visited:
                if not check(i,visited,graph,mapp):
                    return False

        return True
        