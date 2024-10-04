class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n=len(skill)
        skill.sort()
        desired=skill[-1]+skill[0]
        result=0
        if n==2:
            return skill[0]*skill[1]
        else:
            last=n-1
            first=0
            while first<last:
                if skill[first]+skill[last]!=desired:
                    return -1
                result+=skill[first]*skill[last]
                last-=1
                first+=1
        return result
        