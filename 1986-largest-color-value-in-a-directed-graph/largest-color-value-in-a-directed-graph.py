class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        visited=set()
        currentbranch=set()
        n=len(colors)
        routes=defaultdict(list)
        for start,end in edges:
            routes[start].append(end)
        
        def iscycle(node):
            if node in currentbranch:
                return True
            if node in visited:
                return False
            visited.add(node)
            currentbranch.add(node)
            for child in routes[node]:
                if iscycle(child):
                    return True
            currentbranch.remove(node)
            return False

        for nd in range(n):
            if iscycle(nd):
                return -1
        @cache
        def dfs(node):
            branch=defaultdict(int)
            for child in routes[node]:
                calc=dfs(child)
                for k,v in calc.items():
                    branch[k]=max(branch[k],calc[k])
            branch[colors[node]]+=1
            return branch
        maxx=0
        for nd in range(n):
            calc=dfs(nd)
            maxx=max(maxx,max(calc.values()))
        return maxx