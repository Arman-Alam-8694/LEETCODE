
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)  # DP array to store maximum amount robbed up to each house
        
        # Fill the dp array iteratively
        for i in range(1, n + 1):
            dp[i] = nums[i - 1]  # Rob the current house
            for j in range(1, i - 1):  # Check all houses not adjacent to the current house
                dp[i] = max(dp[i], dp[j] + nums[i - 1])
        
        # Maximum amount robbed will be in the last entry of dp
        return max(dp)

