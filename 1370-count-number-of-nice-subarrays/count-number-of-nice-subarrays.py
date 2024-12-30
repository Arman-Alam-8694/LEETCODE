class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        oddarr=[-1]+[i for i in range(n) if nums[i]%2!=0]+[n]
        result=0
        for i in range(1,len(oddarr)-k):
            left=oddarr[i]-oddarr[i-1]
            right=oddarr[i+k]-oddarr[i+k-1]
            result+=left*right
        return result