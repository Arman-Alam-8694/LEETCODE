

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited=set()
        nodes=len(graph)
        terminal_nodes=set()
 
        def dfs(start):
            if start in visited:
                return False
            if start in terminal_nodes:
                return True
            visited.add(start)
            for i in graph[start]:
                if not dfs(i):
                    return False
            visited.remove(start)
            terminal_nodes.add(start)
            return True
            
        result=[]
        for i in range(nodes):
            if dfs(i):
                result.append(i)
        return result

        