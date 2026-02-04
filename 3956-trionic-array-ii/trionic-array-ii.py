from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('-inf')
        i = 0
        
        while i < n:
            # 1. Find peak p (end of increasing segment)
            p = i
            while p + 1 < n and nums[p] < nums[p + 1]:
                p += 1
            
            # Need at least 2 elements in first segment (l < p)
            if p == i:
                i += 1
                continue
            
            # 2. Find valley q (end of decreasing segment)
            q = p
            while q + 1 < n and nums[q] > nums[q + 1]:
                q += 1
            
            # Need valid decreasing segment (p < q) 
            # AND room for third segment (q < r) meaning nums[q] < nums[q+1]
            if q == p or q + 1 >= n or nums[q + 1] <= nums[q]:
                # Move i to q to ensure forward progress and retry
                i = q 
                continue
            
            # 3. Calculate Core Trionic Sum: [p-1 ... q+1]
            # Includes the last step of the first climb, the whole descent, 
            # and the first step of the next climb.
            current_sum = nums[p - 1] + nums[p]
            for k in range(p + 1, q + 2):
                current_sum += nums[k]
            
            # 4. Extend Right: Find max increasing suffix starting at q+2
            # We add to the sum as long as the sequence keeps increasing
            right_max = 0
            right_sum = 0
            k = q + 2
            while k < n and nums[k] > nums[k - 1]:
                right_sum += nums[k]
                right_max = max(right_max, right_sum)
                k += 1
            
            # 5. Extend Left: Find max increasing prefix ending at p-2
            # We scan backwards from p-2 down to i
            left_max = 0
            left_sum = 0
            k = p - 2
            while k >= i:
                left_sum += nums[k]
                left_max = max(left_max, left_sum)
                k -= 1
            
            ans = max(ans, current_sum + left_max + right_max)
            
            # Start the next search from the valley 'q'
            # (The valley of this shape can be the start of the next shape)
            i = q
            
        return ans if ans != float('-inf') else 0