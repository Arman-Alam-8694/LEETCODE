class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # build prefix array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        dp = [float('-inf')] * (n + 1)
        ans = float('-inf')

        # process starting positions of blocks
        for i in range(0, n - k + 1):
            block = prefix[i+k] - prefix[i]   # sum of nums[i : i+k]

            if i - k >= 0:
                dp[i] = max(block, dp[i-k] + block)
            else:
                dp[i] = block  # first possible block (cannot extend)

            ans = max(ans, dp[i])

        return ans

        
        
        