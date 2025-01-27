class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        # Default maximum answer will always be how many "k" integers already exist
        ans = c[k]
        # Only need 1-50 as per the restraints
        for i in range(51):
            # We've already considered i == k in our default answer, and don't care if i not in nums
            if i not in c or i == k:
                continue

            start_sub, score, ks = 0, 0, 0
            while start_sub < len(nums):
                # Current subarray +1
                if nums[start_sub] == i:
                    score += 1
                # Current subarray -1
                elif nums[start_sub] == k:
                    ks += 1

                # Restart if score is negative
                if ks > score:
                    score, ks = 0, 0

                # Subtract number of "k" integers in our subarray from total number that occur
                ans = max(ans, score + (c[k] - ks))
                start_sub += 1

        return ans
                
            