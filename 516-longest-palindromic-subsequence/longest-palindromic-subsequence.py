from functools import cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def recur(sidx,eidx):
            if sidx>eidx:
                return 0
            elif sidx==eidx:
                return 1
            elif s[sidx]==s[eidx]:
                return 2+recur(sidx+1,eidx-1)
            else:
                return max(recur(sidx+1,eidx),recur(sidx,eidx-1))
        return recur(0,len(s)-1)
            
