class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        memo = {}

        def dfs(prev_index, curr_index):
            key = (prev_index, curr_index)
            if curr_index == n:
                return []

            if key in memo:
                return memo[key]

            # Option 1: skip current number
            without = dfs(prev_index, curr_index + 1)

            # Option 2: take current number if divisible
            with_curr = []
            if prev_index == -1 or nums[curr_index] % nums[prev_index] == 0:
                with_curr = [nums[curr_index]] + dfs(curr_index, curr_index + 1)

            # Choose the longer subset
            memo[key] = with_curr if len(with_curr) > len(without) else without
            return memo[key]

        return dfs(-1, 0)
