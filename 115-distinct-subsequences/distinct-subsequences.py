class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @cache
        def recur(cur,sidx):
            if cur==len(t) :
                return 1
            if sidx==len(s):
                return 0
            temp=0
            if t[cur]==s[sidx]:
                temp+=recur(cur+1,sidx+1)
            temp+=recur(cur,sidx+1)
            return temp

        return recur(0,0)
        