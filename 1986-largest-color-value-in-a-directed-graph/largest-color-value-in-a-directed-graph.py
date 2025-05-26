class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        seen=set()
        n=len(colors)
        route=defaultdict(list)

        for i in range(len(edges)):

            route[edges[i][0]].append(edges[i][1])
            # route[edges[i][0]].append(colors[i])

        # print(route)
        visited = set()
        rec_stack = set()

        def dfs(node):
            if node in rec_stack:
                return True
            if node in visited:
                return False
            visited.add(node)
            rec_stack.add(node)
            for neighbor in route[node]:
                if dfs(neighbor):
                    return True
            rec_stack.remove(node)
            return False

        for i in range(n):
            if dfs(i):
                return -1
        @cache  
        def dfs(node):
            # temp=defaultdict(int)
            branch=defaultdict(int)
            # if node==0:
            #     temp[colors[0]]=1
            for child in route[node]:
                calc=dfs(child)
                for k,v in calc.items():
                    branch[k]=max(branch[k],calc[k])
                # print(child,c,branch)
            branch[colors[node]]+=1
            return branch
                

        maxx=float("-inf")
        for i in range(n):
            res=dfs(i)
            maxx=max(maxx,max(res.values()))
        return maxx