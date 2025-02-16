from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # The length of the sequence is (n-1)*2 + 1
        length = (n - 1) * 2 + 1
        sequence = [-1] * length
        used = [False] * (n + 1)  # To track which numbers have been used

        def backtrack(index: int) -> bool:
            if index == length:
                return True  # All positions are filled

            if sequence[index] != -1:
                return backtrack(index + 1)  # Move to the next position

            # Try placing the largest possible number first
            for num in range(n, 0, -1):
                if used[num]:
                    continue  # Skip if the number is already used

                if num == 1:
                    # Place 1 in the current position
                    sequence[index] = 1
                    used[1] = True

                    if backtrack(index + 1):
                        return True

                    # Backtrack
                    sequence[index] = -1
                    used[1] = False
                else:
                    # For numbers greater than 1, check if the second position is available
                    second_pos = index + num
                    if second_pos < length and sequence[second_pos] == -1:
                        sequence[index] = num
                        sequence[second_pos] = num
                        used[num] = True

                        if backtrack(index + 1):
                            return True

                        # Backtrack
                        sequence[index] = -1
                        sequence[second_pos] = -1
                        used[num] = False

            return False  # No valid number could be placed

        backtrack(0)
        return sequence

