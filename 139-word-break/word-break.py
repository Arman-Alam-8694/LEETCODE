from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def find(idx,queue,n):
            for i in range(idx,n):
                if s[idx:i+1] in lookup:
                    queue.append(i)
        queue=deque()
        lookup=set(wordDict)

        n=len(s)
        find(0,queue,n) 
        visited=set()  
      
        if not queue:
            return False
        while queue:
            idx=queue.popleft()
            if idx==n-1:
                return True
            if idx in visited:
                continue
            find(idx+1,queue,n)
            visited.add(idx)
        return False


            