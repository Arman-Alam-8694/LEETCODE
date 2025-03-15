class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        left = 0
        right = len(sorted_nums) - 1
        answer = float('inf')
        
        while left <= right:
            mid = (left + right) // 2
            x = sorted_nums[mid]
            # Check if we can select at least k non-adjacent houses with values <= x
            dp_prev_prev = 0
            dp_prev = 0
            for num in nums:
                if num <= x:
                    current = max(dp_prev, dp_prev_prev + 1)
                else:
                    current = dp_prev
                dp_prev_prev, dp_prev = dp_prev, current
            if dp_prev >= k:
                answer = x
                right = mid - 1
            else:
                left = mid + 1
        return answer