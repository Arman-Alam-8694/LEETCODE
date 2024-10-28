class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_streak = -1
        
        for num in nums:
            current = num
            streak = 1
            
            while (current * current) in nums_set:
                current = current * current
                streak += 1
            
            if streak >= 2:
                max_streak = max(max_streak, streak)
        
        return max_streak if max_streak >= 2 else -1
        