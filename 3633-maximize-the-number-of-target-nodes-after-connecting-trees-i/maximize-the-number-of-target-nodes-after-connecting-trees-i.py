class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n=0
        tree_one=defaultdict(list)
        tree_two=defaultdict(list)        
        for s,e in edges1:
            tree_one[s].append(e)
            tree_one[e].append(s)
            n=max(n,s,e)
        m=0
        for s,e in edges2:
            tree_two[s].append(e)
            tree_two[e].append(s)
            m=max(m,s,e)
    
        def bfs(start,upto,tree):
            count=0
            queue=deque([(start,0)])
            seen=set()
            while queue:
                node,reached=queue.pop()
                count+=1
                seen.add(node)
                if reached==upto:
                    continue
                else:
                    for child in tree[node]:
                        if child not in seen:
                            queue.append((child,reached+1))
            return count
        second=0
        result=[]
        if k==0:
            second=0
        else:
            for i in range(m+1):
                second=max(second,bfs(i,k-1,tree_two))
        for i in range(n+1):
            val=bfs(i,k,tree_one)
            result.append(val+second)
        return result


        





        