from collections import defaultdict

class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        run = 0
        result = 0

        for right in range(len(nums)):
            run += freq[nums[right]]
            freq[nums[right]] += 1

            while run >= k:
                # all subarrays starting from left to right are valid
                result += len(nums) - right
                freq[nums[left]] -= 1
                run -= freq[nums[left]]
                left += 1

        return result
