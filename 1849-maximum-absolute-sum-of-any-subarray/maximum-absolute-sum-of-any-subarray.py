class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        suffix_max = [0] * n  # Maximum suffix sum up to each index
        suffix_min = [0] * n  # Minimum suffix sum up to each index

        # Compute suffix sums from the end
        suffix_max[-1] = nums[-1]
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(nums[i], nums[i] + suffix_max[i + 1])
            suffix_min[i] = min(nums[i], nums[i] + suffix_min[i + 1])

        max_abs_sum = -float('inf')  # Track maximum absolute sum
        current_sum = 0  # Track current subnumsay sum

        # Traverse the numsay from the start
        for i in range(n):
            # Decide whether to extend the current subnumsay or start a new one
            if (current_sum >= 0 and suffix_max[i] >= 0) or (current_sum <= 0 and suffix_min[i] <= 0):
                current_sum += nums[i]
            else:
                current_sum = nums[i]

            # Update maximum absolute sum
            max_abs_sum = max(max_abs_sum, abs(current_sum))

        return max_abs_sum


            