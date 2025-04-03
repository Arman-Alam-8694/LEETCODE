class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        dmax=0
        lmax=0
        maxx=0
        for i in nums:
            maxx=max(maxx,dmax*i)
            dmax=max(dmax,lmax-i)
            lmax=max(lmax,i)
        return maxx
        