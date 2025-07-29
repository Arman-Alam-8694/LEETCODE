# from typing import List

# class Solution:
#     def smallestSubarrays(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         # Step 1: Compute suffix OR for each index
#         suffix_or = [0] * n
#         suffix_or[-1] = nums[-1]
#         for i in range(n - 2, -1, -1):
#             suffix_or[i] = suffix_or[i + 1] | nums[i]

#         answer = [0] * n
#         bit_count = [0] * 32
#         L = 0

#         def current_or():
#             """Construct current OR from bit_count array."""
#             val = 0
#             for b in range(32):
#                 if bit_count[b] > 0:
#                     val |= (1 << b)
#             return val

#         for R in range(n):
#             # Add nums[R]'s set bits to bit_count
#             for b, bit in enumerate(reversed(bin(nums[R])[2:].zfill(32))):
#                 if bit == '1':
#                     bit_count[b] += 1

#             # Shrink from L as long as OR is still sufficient
#             while L <= R and current_or() == suffix_or[L]:
#                 answer[L] = R - L + 1
#                 # Remove nums[L]'s set bits
#                 for b, bit in enumerate(reversed(bin(nums[L])[2:].zfill(32))):
#                     if bit == '1':
#                         bit_count[b] -= 1
#                 L += 1

#         return answer

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = [-1] * 31
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            j = i
            for bit in range(31):
                if (nums[i] & (1 << bit)) == 0:
                    if pos[bit] != -1:
                        j = max(j, pos[bit])
                else:
                    pos[bit] = i
            ans[i] = j - i + 1
        return ans
