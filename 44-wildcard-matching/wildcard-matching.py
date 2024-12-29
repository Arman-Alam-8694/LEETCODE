class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Initialize the dp array with None values
        dp = [[None] * (len(p) + 1) for _ in range(len(s) + 1)]

        def recur(sidx, pidx):
            # If both the string and pattern are fully traversed
            if sidx == len(s) and pidx == len(p):
                return True
            
            # If the pattern is exhausted but the string isn't
            if pidx == len(p):
                return False
            
            # If the string is exhausted but the pattern isn't
            if sidx == len(s):
                # Remaining characters in the pattern must all be '*'
                for c in p[pidx:]:
                    if c != '*':
                        return False
                return True

            # If the result is already computed, return it
            if dp[sidx][pidx] is not None:
                return dp[sidx][pidx]

            # Match the current characters
            if p[pidx] == '?':
                # Match one character
                dp[sidx][pidx] = recur(sidx + 1, pidx + 1)
            elif p[pidx] == '*':
                # Match zero or more characters
                if recur(sidx + 1, pidx):
                    dp[sidx][pidx] = True
                else:
                    dp[sidx][pidx] = recur(sidx, pidx + 1)
            else:
                # Exact match for the current character
                if s[sidx] == p[pidx]:
                    dp[sidx][pidx] = recur(sidx + 1, pidx + 1)
                else:
                    dp[sidx][pidx] = False

            return dp[sidx][pidx]

        return recur(0, 0)
