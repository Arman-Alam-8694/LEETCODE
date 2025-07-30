class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_and=max(nums)
        result=1
        temp=0
        for i in nums:
            if i==max_and:
                temp+=1
            else:
                result=max(result,temp)
                temp=0
        result=max(result,temp)
        return result
        