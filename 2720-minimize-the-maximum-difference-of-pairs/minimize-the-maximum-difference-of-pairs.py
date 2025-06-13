import itertools

class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        nums.sort()
        n=len(nums)
        def check(limit):
            count=0
            idx=0
            while idx<n-1:
                if nums[idx+1]-nums[idx]<=limit:
                    count+=1
                    idx+=1
                idx+=1
            return count

            
        left=0
        right=nums[-1]-nums[0]
        while left<=right:
            mid=(left+right)//2
            if check(mid)>=p:
                right=mid-1
            else:
                left=mid+1
        return left
            