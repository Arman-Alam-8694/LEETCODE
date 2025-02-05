class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        pair=[]
        cnt=0
        n=len(s1)
        for i in range(n):
            if s1[i]!=s2[i]:
                if cnt==1:
                    return False
                elif pair:
                    temp=(s1[i],s2[i])
                    if temp not in pair:
                        return False
                    else:
                        cnt+=1
                        pair=[]
                else:
                    pair.append((s2[i],s1[i]))
        if pair:
            return False
        return True
                                