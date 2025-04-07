class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total&1:
            return False
        target=total//2
        mapp={}
        n=len(nums)
        def subsetpartition(idx,sum):
            if (idx,sum) in mapp:
                return mapp[(idx,sum)]
            if sum>target:
                return False
            if idx==n or sum==target:
                return sum==target
            if subsetpartition(idx+1,sum+nums[idx]) :
                return True
            if subsetpartition(idx+1,sum):
                return True
            mapp[(idx,sum)]=False
            return mapp[(idx,sum)]
        return subsetpartition(0,0)