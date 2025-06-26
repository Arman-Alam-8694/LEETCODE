class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        #BINARY SEARCH OVER THE ANSWER WHICH IS HERE THE LENGTH OF THE SUBSEQUENCE

        n = len(s)
        def canit(x):
            to_remove = n - x
            val = 0
            curr = 1
            for c in s:
                if c == "1" and to_remove > 0:
                    to_remove -= 1
                else:
                    val <<= 1
                    val += int(c) 
                if val > k:
                    return False
            return True
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            if canit(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r