class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left=0
        n=len(nums)
        right=n-1
        while left<=right:
            mid=(left+right)//2
            lelem=(float("-inf") if mid-1<0 else nums[mid-1])
            relem=(float("-inf") if mid+1>=n else nums[mid+1])
            if lelem<nums[mid]>relem:
                return mid
            elif nums[mid]<relem:
                left=mid+1
            else:
                right=mid-1
        