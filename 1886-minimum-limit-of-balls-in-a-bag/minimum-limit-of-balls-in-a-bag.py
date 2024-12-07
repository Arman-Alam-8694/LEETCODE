class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def possible(mid,nums,k):
            count=0
            for num in nums:
                count+=(num-1)//mid
                if count>k:
                    return False
            return True
        left=1
        right=max(nums)
        while left<=right:
            mid=(left+right)//2
            if possible(mid,nums,maxOperations):
                right=mid-1
            else:
                left=mid+1
        return left