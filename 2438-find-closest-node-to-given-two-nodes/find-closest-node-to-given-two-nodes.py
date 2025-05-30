class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # processed=set()
        # cur_path=set()
        result=float("inf")
        nodeone=defaultdict(int)
        nodetwo=defaultdict(int)
        
        # def cycle_check(node):
        #     if node==-1:
        #         return False
        #     if node in cur_path:
        #         return True
        #     cur_path.add(node)
        #     if cycle_check(edges[node]):
        #         return True
        #     return False
        
        # n=len(edges)
        # for i in range(n):
        #     if i not in processed:
        #         cur_path=set()
        #         cycle_check(i)

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
        print(nodeone)
        print(nodetwo)
        answer=float("inf")
        if len(nodeone)<len(nodetwo):
            for u,a in nodeone.items():
                if u in nodetwo:
                    temp=max(a,nodetwo[u])
                    if temp<result:
                        answer=u
                        result=temp
                    elif temp==result:
                        answer=min(answer,u)
        else:
            for u,a in nodetwo.items():
                if u in nodeone:
                    temp=max(a,nodeone[u])
                    if temp<result:
                        answer=u
                        result=temp
                    elif temp==result:
                        answer=min(answer,u)


                    
        return answer if answer!=float("inf") else -1
            
        


        