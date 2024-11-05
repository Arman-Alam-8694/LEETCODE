class Solution:
    def minChanges(self, s: str) -> int:
        count=0
        for i in range(1,len(s),2):
            if int(s[i])^int(s[i-1]):
                count+=1
        return count
        