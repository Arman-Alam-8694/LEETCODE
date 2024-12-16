from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs(graph,start,colors):
            colors={}
            colors[start]=0
            order=deque([start])
            while order:
                node=order.popleft()
                for sons in graph[node]:
                    if sons not in colors:
                        colors[sons]=1-colors[node]
                        order.append(sons)
                    else:
                        if colors[sons]==colors[node]:
                            return False

            return True
        colors={}
        for i in range(len(graph)):
            if i not in colors:
                if not bfs(graph,i,colors):
                    return False
        return True



        
        