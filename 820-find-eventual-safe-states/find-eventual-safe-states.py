class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited=set()
        nodes=len(graph)
        terminal_nodes=set()
        @cache
        def dfs(start):
            if start in visited:
                return False
            visited.add(start)
            if start in terminal_nodes:
                return True
            for i in graph[start]:
                if not dfs(i):
                    return False
            terminal_nodes.add(start)
            return True
            
        result=[]
        for i in range(nodes):
            if dfs(i):
                result.append(i)
        return result

        