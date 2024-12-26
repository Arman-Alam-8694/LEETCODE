class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #2d DP
        # mapp=[defaultdict(int) for _ in range(len(nums)+1)]
        # mapp[0][0]=1
        # for i in range(len(nums)):
        #     for k,v in mapp[i].items():
        #         mapp[i+1][k+nums[i]]+=v
        #         mapp[i+1][k-nums[i]]+=v

        # return mapp[len(nums)][target]
        #1D DP
        mapp=defaultdict(int)
        mapp[0]=1
        for i in range(len(nums)):
            temp=defaultdict(int)
            for k,v in mapp.items():
                temp[k+nums[i]]+=v
                temp[k-nums[i]]+=v
            mapp=temp
        return mapp[target]