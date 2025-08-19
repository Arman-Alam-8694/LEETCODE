class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result=0
        left=0
        for right in range(len(nums)):
            if nums[right]==0:
                result+=(right-left+1)
            else:
                left=right+1
        return result
            

        