from typing import List
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Build transition map
        trans = defaultdict(list)
        for s in allowed:
            trans[s[:2]].append(s[2])

        memo = {}

        def dfs(curr: str) -> bool:
            # Base case
            if len(curr) == 1:
                return True

            # Memo check
            if curr in memo:
                return memo[curr]

            # FAIL-FAST PRUNING
            for i in range(len(curr) - 1):
                if curr[i:i+2] not in trans:
                    memo[curr] = False
                    return False

            def build(idx: int, nxt: List[str]) -> bool:
                if idx == len(curr) - 1:
                    return dfs("".join(nxt))

                pair = curr[idx:idx+2]
                for c in trans[pair]:
                    nxt.append(c)
                    if build(idx + 1, nxt):
                        return True
                    nxt.pop()
                return False

            memo[curr] = build(0, [])
            return memo[curr]

        return dfs(bottom)
