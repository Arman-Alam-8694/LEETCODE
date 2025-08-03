from typing import List

class Solution:
    def maxTotalFruits(
        self, fruits: List[List[int]], startPos: int, k: int
    ) -> int:
        # Build a dense array from position 0 to max needed index
        max_fruit_pos = fruits[-1][0] if fruits else 0
        max_index = max(max_fruit_pos, startPos)
        size = max_index + 1

        # Populate fruit counts at each position
        fruit_at = [0] * size
        for pos, amt in fruits:
            fruit_at[pos] = amt

        # Build prefix sum array
        prefix = [0] * (size + 1)
        for i in range(size):
            prefix[i + 1] = prefix[i] + fruit_at[i]

        ans = 0
        # Try all possible first moves x (0 to k)
        for x in range(k + 1):
            # 1) Move x steps to the left, then (k - x) steps to the right
            left_pos = startPos - x
            if left_pos < 0:
                left_pos = 0
            reach = k - x
            right_pos = left_pos + reach
            if right_pos > max_index:
                right_pos = max_index
            # Collect fruits in [left_pos, right_pos]
            total = prefix[right_pos + 1] - prefix[left_pos]
            ans = max(ans, total)

            # 2) Move x steps to the right, then (k - x) steps to the left
            right_pos = startPos + x
            if right_pos > max_index:
                right_pos = max_index
            reach = k - x
            left_pos = right_pos - reach
            if left_pos < 0:
                left_pos = 0
            total = prefix[right_pos + 1] - prefix[left_pos]
            ans = max(ans, total)

        return ans
