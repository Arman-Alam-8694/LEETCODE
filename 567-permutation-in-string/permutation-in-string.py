class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size=len(s1)
        if len(s1)>len(s2):
            return False
        count=Counter(s1)
        windows=Counter(s2[:size])
        if count==windows:
            return True
        for i in range(1,len(s2)-size+1):
            windows[s2[i-1]]-=1
            if windows[s2[i-1]]==0:
                del windows[s2[i-1]]
            windows[s2[i+size-1]]=windows.get(s2[i+size-1],0)+1
            if count==windows:
                return True
        return False



        