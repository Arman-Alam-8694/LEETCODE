class Solution:
    def minimumLength(self, s: str) -> int:
        mapp=Counter(s)
        result=0
        for k,v in mapp.items():
            if v&1:
                result+=v//2
            else:
                result+=(v-1)//2
        return len(s)-(2*result)
        