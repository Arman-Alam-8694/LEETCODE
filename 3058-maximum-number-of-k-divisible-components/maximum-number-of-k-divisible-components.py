class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        def dfs(node, parent):
            csumm=values[node]
            divisiblecnt=0
            for son in graph[node]:
                if son!=parent:
                    summ,cnt=dfs(son,node)
                    csumm+=summ
                    divisiblecnt+=cnt
     
            if csumm%k==0:
                divisiblecnt+=1
                return [0,divisiblecnt]
            else:
                return [csumm,divisiblecnt]

        # Build the graph from edges
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Start DFS from node 0
        _, cntt = dfs(0, -1)
        return cntt
