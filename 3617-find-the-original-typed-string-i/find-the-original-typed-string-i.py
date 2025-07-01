class Solution:
    def possibleStringCount(self, word: str) -> int:
        n=len(word)
        counts=0
        result=1
        for i in range(n):
            counts+=1
            if i+1==n or (i+1<n and word[i]!=word[i+1]):
                result+=(counts-1)
                counts=0
        return result