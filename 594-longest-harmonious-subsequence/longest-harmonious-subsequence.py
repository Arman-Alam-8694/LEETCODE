class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # nums.sort()
        # n=len(nums)
        # answer=0
        # left=0
        # for right in range(n):
        #     while left<right and nums[right]-1>nums[left]:
        #         left+=1
        #     if nums[left]==nums[right]-1:
        #         answer=max(answer,right-left+1)
        # return answer
        cnts=Counter(nums)
        result=0
        for i,j in cnts.items():
            if i+1 in cnts:
                result=max(result,cnts[i+1]+j)
        return result

        # return result

        