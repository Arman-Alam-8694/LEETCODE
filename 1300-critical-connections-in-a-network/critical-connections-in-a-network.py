class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(graph,node,par,visited,inarr,lowarr):
            nonlocal timer
            nonlocal result
            visited[node]=True
            inarr[node]=timer
            lowarr[node]=timer
            timer+=1
            for child in graph[node]:
                if not visited[child]:
                    dfs(graph,child,node,visited,inarr,lowarr)
                 
                    if lowarr[child]>inarr[node]:
                        result.append([node,child])

                    lowarr[node]=min(lowarr[child],lowarr[node])
                else:
                    if child!=par:
                        lowarr[node]=min(inarr[child],lowarr[node])
                

                
        graph={}
        result=[]
        visited={i:False for i in range(n)}
        for i in range(n):
            graph[i]=[]
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
      
        inarr=["0"]*n
        timer=0
        lowarr=["0"]*n
        dfs(graph,0,-1,visited,inarr,lowarr)
       
        return result