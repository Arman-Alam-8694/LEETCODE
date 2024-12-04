class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        left=0
        s2=len(s)
        if len(t)==len(s):
            for charr in t:
                if charr==s[left]:
                    left+=1
                else:
                    return False
            return True
        
        for charr in t:
            if charr==s[left]:
                left+=1
            if left>=s2:
                return True
        return False

        
        