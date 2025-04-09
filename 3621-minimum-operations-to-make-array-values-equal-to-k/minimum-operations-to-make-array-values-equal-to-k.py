class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        steps=0
        n=len(nums)
        temp=nums[0]
        for i in range(n):
            if nums[i]<k:
                return -1
            if nums[i]!=temp:
                steps+=1
                temp=nums[i]
        return steps+1 if temp>k else steps

        