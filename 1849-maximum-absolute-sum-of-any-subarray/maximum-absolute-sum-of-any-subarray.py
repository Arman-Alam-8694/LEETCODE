from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # n = len(nums)
        # if n == 0:
        #     return 0

        # # Precompute suffix arrays.
        # # For suffix_max, if the next suffix (i+1) is positive, we add it;
        # # otherwise, we “cut off” (i.e. add 0) because a negative extension wouldn’t help a positive current sum.
        # suffix_max = [0] * n
        # suffix_min = [0] * n
        # suffix_max[-1] = nums[-1]
        # suffix_min[-1] = nums[-1]
        # for i in range(n-2, -1, -1):
        #     # When trying to extend a positive sum, add only if the next contribution is positive.
        #     suffix_max[i] = nums[i] + (suffix_max[i+1] if suffix_max[i+1] > 0 else 0)
        #     # When extending a negative sum, add only if the next contribution is negative.
        #     suffix_min[i] = nums[i] + (suffix_min[i+1] if suffix_min[i+1] < 0 else 0)

        # # Initialize our running sum with the first element.
        # current_sum = nums[0]
        # ans = abs(current_sum)
        
        # # Process the array from left to right.
        # for i in range(0, n-1):
        #     # Look ahead: if current_sum is nonnegative, then the optimal extension available is suffix_max;
        #     # if current_sum is negative, then we use suffix_min.
        #     if current_sum >= 0:
        #         potential_extension = suffix_max[i+1]
        #     else:
        #         potential_extension = suffix_min[i+1]
            
        #     # The "future potential" absolute value we could achieve if we optimally extend is:
        #     potential_total = current_sum + potential_extension
            
        #     # Now decide: compare simply starting fresh at index i+1 versus extending current_sum by nums[i+1].
        #     # In other words, if the absolute value of the next element alone is at least as high as what we’d get
        #     # by continuing our current subarray (using our lookahead), then start a new subarray.
        #     if abs(nums[i+1]) >= abs(potential_total):
        #         current_sum = nums[i+1]
        #     else:
        #         current_sum += nums[i+1]
            
        #     # Update the answer with the best absolute sum so far.
        #     ans = max(ans, abs(current_sum))
            
        # return ans


        max_sum = 0  # Tracks the maximum subarray sum
        min_sum = 0  # Tracks the minimum subarray sum
        curr_max = 0  # Running maximum sum
        curr_min = 0  # Running minimum sum

        for num in nums:
            # Kadane's for maximum sum subarray
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)
            
            # Kadane's for minimum sum subarray
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)
        
        # Return the max absolute sum
        return max(abs(max_sum), abs(min_sum))
