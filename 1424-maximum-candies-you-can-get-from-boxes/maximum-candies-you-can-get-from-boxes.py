from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int],
                   keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        result = 0
        seen = set(initialBoxes)
        used = [False] * 1000
        has_key = [False] * 1000

        def dfs(box):
            nonlocal result
            # Skip if already used or cannot be opened
            if used[box] or (status[box] == 0 and not has_key[box]):
                return

            used[box] = True
            result += candies[box]

            # Add keys and try to use them
            for key in keys[box]:
                has_key[key] = True
                # Try opening this box if we already have it
                if key in seen:
                    dfs(key)

            # Explore all contained boxes
            for new_box in containedBoxes[box]:
                seen.add(new_box)
                dfs(new_box)

        for box in initialBoxes:
            dfs(box)

        return result
