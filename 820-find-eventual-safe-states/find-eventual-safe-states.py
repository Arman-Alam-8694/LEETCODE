class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited=set()
        nodes=len(graph)
        terminal_nodes=set([x for x in range(nodes) if graph[x]==[]])
        @cache
        def dfs(start):
          
            if start in visited:
                return False
            visited.add(start)
            if start in terminal_nodes:
                return True
            answer=True
            for i in graph[start]:
           
                answer=answer&dfs(i)
            return answer
            
         

        result=[]
        for i in range(nodes):

            if dfs(i):
                result.append(i)
              

        return result

        