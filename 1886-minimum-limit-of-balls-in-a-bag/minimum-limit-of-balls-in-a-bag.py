class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def possible(mid,nums,k):
            count=0
            for i in range(len(nums)):
                quot,rem=divmod(nums[i],mid)
                if rem==0:
                    count+=quot-1
                else:
                    count+=quot
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