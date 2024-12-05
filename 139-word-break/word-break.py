from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue=deque([0])
        lookup=set(wordDict)
        n=len(s)
        visited=set()  

        while queue:
            idx=queue.popleft()
            if idx==n:
                return True
            if idx in visited:
                continue
            for i in range(idx,n+1):
                if s[idx:i] in lookup:
                    queue.append(i)
            visited.add(idx)
            
        return False


            