from math import gcd
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        
        for num in nums:
            stack.append(num)
            
            # keep merging while top 2 are non-coprime
            while len(stack) > 1:
                a, b = stack[-2], stack[-1]
                g = gcd(a, b)
                if g == 1:
                    break  # coprime → stop merging
                
                # merge into lcm
                lcm = (a * b) // g
                stack.pop()
                stack[-1] = lcm
        
        return stack
