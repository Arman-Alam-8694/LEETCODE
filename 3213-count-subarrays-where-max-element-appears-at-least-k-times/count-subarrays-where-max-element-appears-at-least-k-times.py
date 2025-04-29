class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxx=max(nums)
        left=0
        times=0
        res=0
        for right in range(len(nums)):
            if nums[right]==maxx:
                times+=1
            while times==k and left<=right:
                if nums[left]==maxx:
                    times-=1
                left+=1
            res+=(left)
        return res

        