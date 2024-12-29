class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        """dp[i][j] = ways to form target[:j+1] from letters[:i+1]"""
        n = len(words[0])
        m = len(target)
        if m > n:
            return 0

        d = dict(zip("abcdefghijklmnopqrstuvwxyz", range(26)))

        # letter[i] = how many of each letter at index i
        letters = [[0] * 26 for _ in range(n)]
        for word in words:
            for i in range(n):
                letters[i][d[word[i]]] += 1

        dp = [0] * (m + 1)
        dp[-1] = 1

        for i in range(n):
            new = [0] * (m + 1)
            new[-1] = 1

            for j in range(m):
                if i < j:
                    break

                # skip + use
                new[j] = (dp[j] + letters[i][d[target[j]]] * dp[j - 1]) % 1000000007

            dp = new

        return dp[-2] % 1000000007