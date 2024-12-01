class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length=0
        n=len(s)
        found=False
        for i in range(n-1,-1,-1):
            if s[i]!=" ":
                length+=1
                found=True
            elif found:
                return length
        return length
            
        