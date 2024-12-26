class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mapp=[defaultdict(int) for _ in range(len(nums)+1)]
        mapp[0][0]=1
        for i in range(len(nums)):
            for k,v in mapp[i].items():
                mapp[i+1][k+nums[i]]+=v
                mapp[i+1][k-nums[i]]+=v

        return mapp[len(nums)][target]