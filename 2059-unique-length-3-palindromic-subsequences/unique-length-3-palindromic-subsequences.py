class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res=0
        n=len(s)
        for i in "abcdefghijklmnopqrstuvwxyz":
            first,last=s.find(i),s.rfind(i)
        
            if first!=-1 and last!=-1 and first<last:
                res+=len(set(s[first+1:last]))
        return res
