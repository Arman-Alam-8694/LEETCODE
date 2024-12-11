class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        n=len(nums)
        for right in range(n):
            if nums[right]-nums[left]>k*2:
                left+=1
        return n-left
