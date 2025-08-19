class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result=0
        left=0
        for right in range(len(nums)):
            if not nums[right]==0:
                n=right-left
                result+=(n*(n+1))//2
                left=right+1
        if left < len(nums):
            n = len(nums) - left
            result += (n * (n + 1)) // 2
        return result
            

        