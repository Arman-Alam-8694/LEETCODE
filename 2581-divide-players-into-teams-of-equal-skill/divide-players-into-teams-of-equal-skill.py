class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        count=Counter(skill)
        n=len(skill)
        minn=min(skill)
        maxx=max(skill)
        desired=minn+maxx
        result=0
        visited=set()
        if n==2:
            return minn*maxx
        else:
            for i in skill:
                if i not in visited:

                    if count[i]!=count[desired-i]:
                        return -1
                    if i!=desired-i:
                        result+=(i*(desired-i))*count[i]
                        visited.add(i)
                        visited.add(desired-i)
                    else:
                        result+=(i*i)*(count[i]//2)
                        visited.add(i)
        return result
        