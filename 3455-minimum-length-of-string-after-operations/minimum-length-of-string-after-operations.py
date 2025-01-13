class Solution:
    def minimumLength(self, s: str) -> int:
        mapp=defaultdict(int)
        result=0
        for i in s:
            mapp[i]+=1
            if mapp[i]==3:
                result+=1
                mapp[i]-=2
        return len(s)-(2*result)
        