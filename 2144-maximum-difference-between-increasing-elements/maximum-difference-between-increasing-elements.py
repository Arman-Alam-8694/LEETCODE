class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minn=nums[0]
        maxx=nums[0]
        answer=float("-inf")
        for i in range(len(nums)):
            answer=max(answer,nums[i]-minn)
            minn=min(minn,nums[i])
        return answer if answer!=0 else -1
        