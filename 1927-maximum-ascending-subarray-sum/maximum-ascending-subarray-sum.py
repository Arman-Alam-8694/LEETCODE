class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum=nums[0]
        temp=nums[0]
        n=len(nums)
        for i in range(1,n):
            if nums[i-1]<nums[i]:
                temp+=nums[i]
            else:
                temp=nums[i]
            max_sum=max(max_sum,temp)
        return max_sum

        