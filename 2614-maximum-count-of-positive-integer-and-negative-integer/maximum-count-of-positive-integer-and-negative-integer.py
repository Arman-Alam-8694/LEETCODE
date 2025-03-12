class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        maxp=0
        maxn=0
        for i in nums:
            if i<0:
                maxn+=1
            elif i>0:
                maxp+=1
        return max(maxn,maxp)
        