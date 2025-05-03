class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        mapp=defaultdict(int)
        candidates=set()
        n=len(tops)
        for i,j in zip(tops,bottoms):
            if i==j:
                mapp[i]+=1
                if mapp[i]>=n:
                    candidates.add(i)

            else:
                mapp[i]+=1
                if mapp[i]>=n:
                    candidates.add(i)
                mapp[j]+=1
                if mapp[j]>=n:
                    candidates.add(j)
            
        # print(candidates)
        if not candidates:
            return -1
        minn=n
        for c in candidates:
            temp=max(tops.count(c),bottoms.count(c))
            minn=min(minn,n-temp)
        return minn