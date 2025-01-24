

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #DFS SOLUTION 

        # visited=set()
        # nodes=len(graph)
        # terminal_nodes=set()
 
        # def dfs(start):
        #     if start in visited:
        #         return False
        #     if start in terminal_nodes:
        #         return True
        #     visited.add(start)
        #     for i in graph[start]:
        #         if not dfs(i):
        #             return False
        #     visited.remove(start)
        #     terminal_nodes.add(start)
        #     return True
            
        # result=[]
        # for i in range(nodes):
        #     if dfs(i):
        #         result.append(i)
        # return result

        #TOPOSORT SOLUTION

        nodes=len(graph)
        d=[[] for _ in range(nodes)]
        outdegree,stack=[],[]
        for node,neighbor in enumerate(graph):
            for n in neighbor:
                d[n].append(node)
            outdegree.append(len(neighbor))
            if len(neighbor)==0:
                stack.append(node)

        result=[]
        while stack:
            node=stack.pop()
            result.append(node)
            for n in d[node]:
                outdegree[n]-=1
                if outdegree[n]==0:
                    stack.append(n)

        return sorted(result)