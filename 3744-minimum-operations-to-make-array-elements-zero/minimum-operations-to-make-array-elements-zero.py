import math

class Solution:
    def minOperations(self, queries):
        def prefix_steps(n: int) -> int:
            if n == 0:
                return 0
            k = int(math.log(n, 4))
            # sum of all full blocks before k
            # formula: sum_{i=0}^{k-1} (i+1)*3*4^i
            if k > 0:
                full = 3 * ( (1 - (k+1)*4**k + k*4**(k+1)) // 9 )
            else:
                full = 0
            # last partial block
            last = (n - 4**k + 1) * (k+1)
            return full + last

        ans = 0
        for l, r in queries:
            total = prefix_steps(r) - prefix_steps(l-1)
            ans += (total + 1) // 2
        return ans
