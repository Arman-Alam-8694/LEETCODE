class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        even = n // 2
        odd = n - even
        return (pow(5, odd, mod) * pow(4, even, mod)) % mod
