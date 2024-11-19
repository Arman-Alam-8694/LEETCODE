class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        mapp={}
        left=0
        n=len(nums)
        maxx=0
        summ=0
        for right in range(n):
            while len(mapp)==k or (nums[right] in mapp):
                summ-=nums[left]
                del mapp[nums[left]]
                left+=1
            
            if nums[right] not in mapp:
                summ+=nums[right]
                mapp[nums[right]]=1
            # print(summ)
            # print(mapp)
            if len(mapp)==k:
                maxx=max(maxx,summ)
        return maxx
            
    
            
        