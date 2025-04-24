class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total=len(set(nums))
        mapp={}
        left=0
        n=len(nums)
        result=0
        for right in range(n):
            if nums[right] not in mapp:
                mapp[nums[right]]=0
            mapp[nums[right]]+=1
            while len(mapp)>=total:
                result+=(n-right)
                mapp[nums[left]]-=1
                if mapp[nums[left]]==0:
                    del mapp[nums[left]]
                left+=1
        return result

        