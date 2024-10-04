class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        count=Counter(skill)
        n=len(skill)
        minn=min(skill)
        maxx=max(skill)
        desired=minn+maxx
        result=0
        if n==2:
            return minn*maxx
        else:
            for i in skill:
                if i in count:
                    b=desired-i
                    if b in count:
                        count[b]-=1
                        count[i]-=1
                        if count[b]==0:
                            del count[b]
                        if count[i]==0:
                            del count[i]
                        result+=i*b
                    else:
                        return -1
        return result
        