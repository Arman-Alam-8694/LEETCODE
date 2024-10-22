class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        sett=set()
        n=len(s)
        ans=0
        def backtrack(i):
            nonlocal ans
            nonlocal sett
            if i==n:
                return len(sett)
            for end in range(i,n):
                substring=s[i:end+1]
                if substring not in sett:
                    sett.add(substring)
                    ans=max(ans,backtrack(end+1))
                    sett.remove(substring)
            return ans
        
        backtrack(0)
        return ans