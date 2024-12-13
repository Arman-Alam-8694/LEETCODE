class Solution:
    def findScore(self, nums: List[int]) -> int:
        new=[(j,i) for i,j in enumerate(nums)]
        new.sort()
        seen=set()
        score=0
        for val,idx in new:
            if idx not in seen:
                score+=val
                seen.add(idx-1)
                seen.add(idx+1)
        return score

