class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        n = len(nums)

        if maxK < minK:
            return 0
        
        prev_bad = [-1] * n
        next_bad = [n] * n

        last_invalid = -1
        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                last_invalid = i
            prev_bad[i] = last_invalid

        last_invalid = n
        for i in range(n-1, -1, -1):
            if nums[i] < minK or nums[i] > maxK:
                last_invalid = i
            next_bad[i] = last_invalid

        ans = 0
        last_minK = -1
        last_maxK = -1
        left = -1  # start left pointer

        for i in range(n):
            if nums[i] == minK:
                last_minK = i
            if nums[i] == maxK:
                last_maxK = i

            valid_start = min(last_minK, last_maxK)
            
            # Window is valid if valid_start > prev_bad[i]
            if valid_start > prev_bad[i]:
                left_choices = valid_start - max(left, prev_bad[i])
                right_choices = next_bad[i] - i
                ans += left_choices * right_choices

                left = valid_start  # move left to valid_start (important)
            
        return ans
