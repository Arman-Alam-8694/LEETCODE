class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        k+=1
        heap=[]
        heap.append((0,0,src))
        adj=[[] for _ in range(n)]
        for i,j,c in flights:
            adj[i].append((j,c))
        visited=[0]*n
        # print(adj)

        while heap:
            cost,step,node=heapq.heappop(heap)
            if node==dst and step<=k:
                return cost
            
            if not visited[node]:
            
                visited[node]=step
            elif visited[node]>step:
               
                visited[node]=step
            else:
                continue
            if step>=k:
                continue
            for nv,c in adj[node]:
                # print(nv,c)
                heapq.heappush(heap,(cost+c,step+1,nv))

        return -1

            
            


        