class Solution:
    def maxDifference(self, s: str) -> int:
        maxx=0
        n=len(s)
        mapp=Counter(s)
        od_max=1
        even_min=n
        for k,v in mapp.items():
            if v&1:
                od_max=max(od_max,v)
            else:
                even_min=min(even_min,v)
        return od_max-even_min

        