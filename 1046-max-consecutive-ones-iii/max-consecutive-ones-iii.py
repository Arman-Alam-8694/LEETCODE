class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        def check(size,nums,k):
            left=0
            zeroes=0
            ones=0
            for right in range(len(nums)):
                if nums[right]==0:
                    zeroes+=1
                else:
                    ones+=1
                if ((right-left)+1)>=size:
                    if zeroes<=k:
                        return True
                    if nums[left]==0:
                        zeroes-=1
                    else:
                        ones-=1
                    left+=1
            return False
        
            
        low=0
        n=len(nums)
        high=n
        while low<=high:
            mid=(low+high)//2
            if check(mid,nums,k):
                low=mid+1
            else:
                high=mid-1
        return high if high!=-1 else 0

