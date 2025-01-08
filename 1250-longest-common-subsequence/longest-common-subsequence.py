class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def recur(a,b):
            if a==-1 or b==-1:
                return 0
            if text1[a]==text2[b]:
                return 1+recur(a-1,b-1)
            return 0+max(recur(a-1,b),recur(a,b-1))
        return recur(len(text1)-1,len(text2)-1)