class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
     
        dp = [float('-inf')] * (n + 1)
        ans = float('-inf')

        for i in range(k-1 ,n):
            blockSum = prefix[i+1] - prefix[i - k+1]
            dp[i] = max(blockSum, dp[i - k] + blockSum)
            ans = max(ans, dp[i])

        return ans
            