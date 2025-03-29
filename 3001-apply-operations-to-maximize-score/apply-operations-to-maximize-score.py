from collections import defaultdict, deque
from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(nums)

        # Step 1: Function to count distinct prime factors (Kept Unchanged)
        def count_distinct_prime_factors(n):
            count = 0
            if n % 2 == 0:
                count += 1
                while n % 2 == 0:
                    n //= 2
            factor = 3
            while factor * factor <= n:
                if n % factor == 0:
                    count += 1
                    while n % factor == 0:
                        n //= factor
                factor += 2
            if n > 1:
                count += 1
            return count

        # Step 2: Compute prime factors count and store occurrences
        prime_scores = [count_distinct_prime_factors(num) for num in nums]

        # Step 3: Compute next and previous dominant indices using monotonic stacks
        next_dominant = [n] * n
        prev_dominant = [-1] * n
        stack = deque()

        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                next_dominant[stack.pop()] = i
            if stack:
                prev_dominant[i] = stack[-1]
            stack.append(i)

        # Step 4: Compute contribution of each number
        num_of_subarrays = [(next_dominant[i] - i) * (i - prev_dominant[i]) for i in range(n)]

        # Step 5: Sort numbers in descending order
        sorted_nums = sorted(enumerate(nums), key=lambda x: -x[1])

        # Step 6: Compute result using fast exponentiation
        res = 1
        for idx, num in sorted_nums:
            if k == 0:
                break
            operations = min(k, num_of_subarrays[idx])
            res = (res * pow(num, operations, mod)) % mod
            k -= operations

        return res
