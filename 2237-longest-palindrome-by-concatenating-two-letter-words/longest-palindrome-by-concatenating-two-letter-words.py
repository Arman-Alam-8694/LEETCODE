class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = defaultdict(int)
        result = 0
        has_center = False

        for w in words:
            rev = w[::-1]
            if count[rev] > 0:
                result += 4
                count[rev] -= 1
            else:
                count[w] += 1

        # Check for a central word like "gg" that can sit in the middle
        for w in count:
            if w[0] == w[1] and count[w] > 0:
                has_center = True
                break

        return result + 2 if has_center else result
