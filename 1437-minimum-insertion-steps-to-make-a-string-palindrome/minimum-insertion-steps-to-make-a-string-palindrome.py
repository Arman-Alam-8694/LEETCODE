from functools import cache

class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def longestPalindromeSubseq(start: int, end: int) -> int:
            if start > end:
                return 0
            if start == end:
                return 1
            if s[start] == s[end]:
                return 2 + longestPalindromeSubseq(start + 1, end - 1)
            return max(longestPalindromeSubseq(start + 1, end),
                       longestPalindromeSubseq(start, end - 1))
        
        n = len(s)
        lps = longestPalindromeSubseq(0, n - 1)
        return n - lps
