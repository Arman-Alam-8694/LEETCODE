class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def formword(idx1,idx2):
            if idx1==len(word1):
                return len(word2)-idx2
            if idx2==len(word2):
                return len(word1)-idx1
            if word1[idx1]==word2[idx2]:
                skip=formword(idx1+1,idx2+1)
            else:
                skip=float('inf')
            insert=1+formword(idx1,idx2+1)
            delete=1+formword(idx1+1,idx2)
            replace=1+formword(idx1+1,idx2+1)
            return min(insert,delete,replace,skip)


        return formword(0,0)
        