from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(st: str) -> bool:
            balance = 0
            for ch in st:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    if balance == 0:
                        return False
                    balance -= 1
            return balance == 0

        res = []
        visited = {s}
        queue = deque([s])
        found = False

        while queue:
            curr = queue.popleft()
            if is_valid(curr):
                res.append(curr)
                found = True
            if found:
                # once we found valid strings at this level, don't go deeper
                continue
            for i in range(len(curr)):
                if curr[i] not in ('(', ')'):
                    continue
                nxt = curr[:i] + curr[i+1:]
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return res

# Example usage:
# sol = Solution()\#
# print(sol.removeInvalidParentheses("()())()"))  # ["(())()", "()()()"]