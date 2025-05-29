class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        treeone=defaultdict(list)
        treetwo=defaultdict(list)
        nodeclr=defaultdict(str)
        for s,e in edges1:
            treeone[s].append(e)
            treeone[e].append(s)
        for s,e in edges2:
            treetwo[s].append(e)
            treetwo[e].append(s)
        
        def colour(start,tree,save):
            queue=deque([(start,"red")])
            seen=set()
            redcnt=0
            bluecnt=0
            while queue:
                node,prevcolor=queue.popleft()
                seen.add(node)
                if prevcolor=="red":
                    redcnt+=1
                else:
                    bluecnt+=1
                if save:
                    nodeclr[node]=prevcolor
                for child in tree[node]:
                    if child not in seen:
                        queue.append((child,"blue" if prevcolor=="red" else "red"))
            if save:
                return redcnt,bluecnt
            else:
                return max(redcnt,bluecnt)
           
        r,b=colour(0,treeone,True)
        fast={"red":r,"blue":b}
        result=[]
        smax=colour(0,treetwo,False)
        n=max(treeone.keys())
        for i in range(n+1):
            result.append(fast[nodeclr[i]]+smax)

        return result
        