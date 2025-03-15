from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left,right=min(nums),max(nums)
        n=len(nums)
        def canRob(cap):
            count=0
            i=0
            while i<n:
                if nums[i]<=cap:
                    count+=1
                    i+=1
                i+=1

                if count>=k:
                    return True
            return False


        res=0
        while left<=right:
            mid=(left+right)//2
            if canRob(mid):
                res=mid
                right=mid-1
            else:
                left=mid+1
        return res