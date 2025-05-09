from functools import lru_cache

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        digits = list(map(int, num))
        total = sum(digits)

        # If the sum is odd, no balanced split
        if total % 2 != 0:
            return 0
        # (Uncomment if halves must be same length for odd n)
        # if n % 2 != 0:
        #     return 0

        half_sum = total // 2
        half_len = n // 2

        # Count occurrences of each digit
        counts = [0]*10
        for d in digits:
            counts[d] += 1

        # Precompute factorials & inverse factorials
        fact    = [1]*(n+1)
        invfact = [1]*(n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1] * i % MOD
        invfact[n] = pow(fact[n], MOD-2,MOD)
        for i in range(n, 0, -1):
            invfact[i-1] = invfact[i] * i % MOD

        @lru_cache(None)
        def dfs(digit, slots_left, sum_left):
            # used up digits 0..9?
            if digit < 0:
                return 1 if (slots_left == 0 and sum_left == 0) else 0
            # prune impossible
            if slots_left < 0 or sum_left < 0:
                return 0

            ways = 0
            max_use = min(counts[digit], slots_left)
            for use in range(max_use+1):
                cost = digit * use
                if cost > sum_left:
                    break

                # **new**: number of ways to pick *which* `use` copies of this digit
                choose = fact[counts[digit]]
                choose = choose * invfact[use] % MOD
                choose = choose * invfact[counts[digit] - use] % MOD

                ways = (ways +
                        choose *
                        dfs(digit-1, slots_left-use, sum_left-cost)
                       ) % MOD

            return ways

        # count ways to select the "first half" (including copy-choices)
        ways = dfs(9, half_len, half_sum)

        # multiply by permutations of each half
        res = ways * fact[half_len] % MOD
        res = res * fact[n-half_len] % MOD

        # divide out global duplicates
        for c in counts:
            res = res * invfact[c] % MOD

        return res
