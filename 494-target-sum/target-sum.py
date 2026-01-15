class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:


        @cache
        def recur(i,curr):
            
            if i==len(nums):
                if curr==target:
                    return 1
                return 0

            branch=0

            #make positive
            branch+=recur(i+1,curr+nums[i])
            branch+=recur(i+1,curr-nums[i])
            return branch
        return recur(0,0)