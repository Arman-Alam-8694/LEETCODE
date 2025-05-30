class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        result=float("inf")
        nodeone=defaultdict(int)
        nodetwo=defaultdict(int)
        def find_path(node,cost,path,seen):
            if node==-1:
                return 
            if node in seen:
                return 
            seen.add(node)
            path[node]=cost
            return find_path(edges[node],cost+1,path,seen)
        
        find_path(node1,0,nodeone,set())
        find_path(node2,0,nodetwo,set())
        answer=float("inf")
        for u,a in nodetwo.items():
            if u in nodeone:
                temp=max(a,nodeone[u])
                if temp<result:
                    answer=u
                    result=temp
                elif temp==result:
                    answer=min(answer,u)   
        return answer if answer!=float("inf") else -1
            
        


        