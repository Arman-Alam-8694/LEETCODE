from typing import List
from collections import deque

class Solution:
    MOD = int(1e9 + 7)

    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Step 1: Find all prime numbers up to max(nums) using Sieve of Eratosthenes
        max_element = max(nums)
        primes = self.get_primes(max_element)

        # Step 2: Compute prime factor count for each element
        prime_scores = [self.count_distinct_prime_factors(num, primes) for num in nums]

        # Step 3: Compute next and previous dominant indices using monotonic stack
        next_dominant = [n] * n
        prev_dominant = [-1] * n
        stack = deque()

        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                next_dominant[stack.pop()] = i
            prev_dominant[i] = stack[-1] if stack else -1
            stack.append(i)

        # Step 4: Compute number of subarrays where each element is dominant
        num_of_subarrays = [(next_dominant[i] - i) * (i - prev_dominant[i]) for i in range(n)]

        # Step 5: Sort elements by value in decreasing order
        sorted_array = sorted(enumerate(nums), key=lambda x: -x[1])

        score = 1

        # Step 6: Process elements to maximize product
        for i, num in sorted_array:
            if k == 0:
                break
            times = min(k, num_of_subarrays[i])
            score = (score * pow(num, times, self.MOD)) % self.MOD
            k -= times

        return score

    # Function to get all primes up to a limit using Sieve of Eratosthenes
    def get_primes(self, limit: int) -> List[int]:
        is_prime = [True] * (limit + 1)
        primes = []

        for num in range(2, limit + 1):
            if is_prime[num]:
                primes.append(num)
                for multiple in range(num * num, limit + 1, num):
                    is_prime[multiple] = False

        return primes

    # Function to count distinct prime factors of a number using precomputed primes
    def count_distinct_prime_factors(self, num: int, primes: List[int]) -> int:
        count = 0
        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                count += 1
                while num % prime == 0:
                    num //= prime
        if num > 1:
            count += 1  # Remaining number itself is a prime
        return count
