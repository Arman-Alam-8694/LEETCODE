from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        def dfs(op_index: int, k: int, char: str) -> str:
            if op_index < 0:
                return char

            op = operations[op_index]

            # Get the length of the word before this operation
            length = lengths[op_index]

            if k <= length:
                # The k-th character came from the first half (original part)
                return dfs(op_index - 1, k, char)
            else:
                # The k-th character came from the second half
                if op == 0:
                    # Second half is identical to first
                    return dfs(op_index - 1, k - length, char)
                else:
                    # Second half is shifted version
                    ch = dfs(op_index - 1, k - length, char)
                    return chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))

        # Precompute the lengths after each operation
        lengths = [1]  # length after each step
        for op in operations:
            prev = lengths[-1]
            if prev > 1e18:  # prevent overflow
                lengths.append(int(1e18))
            else:
                lengths.append(prev * 2)

        return dfs(len(operations) - 1, k, 'a')
