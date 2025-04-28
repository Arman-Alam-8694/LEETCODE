from functools import lru_cache

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        s_rev = s[::-1]

        @lru_cache(maxsize=None)
        def lcs(i: int, j: int) -> int:
            if i == 0 or j == 0:
                return 0
            if s[i - 1] == s_rev[j - 1]:
                return 1 + lcs(i - 1, j - 1)
            return max(lcs(i - 1, j), lcs(i, j - 1))

        longest_palindromic_subseq = lcs(n, n)
        return n - longest_palindromic_subseq
