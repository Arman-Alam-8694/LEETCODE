class Solution:
    def maxFrequency(self, nums, k):
        cnt = [0] * 51  # Initialize a list of 51 zeros
        res = 0
        cnt_k = 0

        for n in nums:
            cnt[n] = max(cnt[n], cnt_k) + 1
            res += (n == k)  # Equivalent to res += 1 if n == k else 0
            cnt_k += (n == k)
            res = max(res, cnt[n])

        return res