class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        result, used = ["-1"] * (n + 1), set()

        def backtrack(idx, start):
            if idx == n + 1:
                return True
            for i in (range(start, n + 2) if idx == 0 or pattern[idx - 1] == "I" else range(start, 0, -1)):
                if i not in used:
                    result[idx] = str(i)
                    used.add(i)
                    if backtrack(idx + 1, i):
                        return True
                    used.remove(i)
            return False

        backtrack(0, 1)
        return "".join(result)
