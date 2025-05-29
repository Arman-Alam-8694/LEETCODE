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
                if node in seen:
                    continue
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
            return redcnt,bluecnt
           
        r,b=colour(0,treeone,True)
        fast={"red":r,"blue":b}
        result=[]
        sred,sblue=colour(0,treetwo,False)
        smax=max(sred,sblue)
        n=max(treeone.keys())
        # print(smax)
        for i in range(n+1):
            result.append(fast[nodeclr[i]]+smax)

        return result
        