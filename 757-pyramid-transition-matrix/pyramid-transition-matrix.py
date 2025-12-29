from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Build transition map
        mapp = {}
        for s in allowed:
            key = s[:2]
            if key not in mapp:
                mapp[key] = []
            mapp[key].append(s[2])

        memo = {}

        def backtrack(stage, i, j, bottom, nxt):
            # Base case
            if stage == 1:
                return True

            # ✅ Memoization on full row only
            bottom="".join(bottom)
            if i == 0 and j == 1 and bottom in memo:
                return memo[bottom]

            # ✅ Fail-fast pruning on full row
            if i == 0 and j == 1:
                for x in range(len(bottom) - 1):
                    if bottom[x] + bottom[x + 1] not in mapp:
                        memo[bottom] = False
                        return False

            temp = bottom[i] + bottom[j]

            if temp in mapp:
                for ch in mapp[temp]:
                    nxt.append(ch)

                    # Finished building next row
                    if j == stage - 1:
                        if backtrack(stage - 1, 0, 1, nxt, []):
                            memo[bottom] = True
                            return True
                    else:
                        if backtrack(stage, i + 1, j + 1, bottom, nxt):
                            return True

                    nxt.pop()

            # Cache result
            if i == 0 and j == 1:
                memo[bottom] = False

            return False

        return backtrack(len(bottom), 0, 1, bottom, [])
