class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp={}
        @cache
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
                return all(c == '*' for c in p[pidx:])

            # Match the current characters
            if p[pidx] == '?':
                # Match one character
                return recur(sidx + 1, pidx + 1)
            elif p[pidx] == '*':
                # Match zero or more characters
                return recur(sidx + 1, pidx) or recur(sidx, pidx + 1)
            else:
                # Exact match for the current character
                return s[sidx] == p[pidx] and recur(sidx + 1, pidx + 1)

        return recur(0, 0)
