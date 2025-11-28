class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        answer=[0]
        def dfs(curr):
       
            if not visited[curr]:
                visited[curr]=True
                temp=values[curr]
                for i in path[curr]:
                    if not visited[i]:
                        print("double",i)
                        temp+=dfs(i)
                    print("first",curr)
                    visited[i]=True
                visited[curr]=True
                if temp%k==0:
                    answer[0]+=1
                    return 0
                else:
                    return temp
            else:
                return 0
        


        
        visited=[False for _ in range(n)]
        counted=set()
        path=[[] for _ in range(n)]
        for i,j in edges:
            path[i].append(j)
            path[j].append(i)
        
        dfs(0)
       
        
        return answer[0]
        