class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        maxx=float("-inf")
        for right in range(len(nums)):
            while  nums[right]-nums[left]>k*2:
                left+=1
            maxx=max(maxx,(right-left+1))
        return maxx
