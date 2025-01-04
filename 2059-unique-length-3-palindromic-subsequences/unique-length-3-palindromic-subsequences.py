class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        chrr=set(s)
        res=0
        n=len(s)
        for i in chrr:
            first,last=s.index(i),s.rindex(i)
            middle=set()
            for i in range(first+1,last):
                middle.add(s[i])
            res+=len(middle)
        return res
