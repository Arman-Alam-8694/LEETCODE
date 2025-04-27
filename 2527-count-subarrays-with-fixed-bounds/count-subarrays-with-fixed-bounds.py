class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        bad=-1
        minn=-1
        maxx=-1
        res=0
        for right in range(len(nums)):
            if nums[right]==minK:
                minn=right
            if nums[right]==maxK:
                maxx=right
            elif not minK<=nums[right]<=maxK:
                bad=right
            if minn!=-1 and maxx!=-1:
                # print(min(0,min(minn,maxx)-bad))
                res+=max(0,min(minn,maxx)-bad)
        return res




