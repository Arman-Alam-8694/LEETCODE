class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res,left,summ,cnt=0,0,0,0
        for right in range(len(nums)):
            summ+=nums[right]
            cnt+=1
            while summ*cnt>=k and left<=right:
                summ-=nums[left]
                cnt-=1
                left+=1
            res+=(right+1)-left 
        return res


        