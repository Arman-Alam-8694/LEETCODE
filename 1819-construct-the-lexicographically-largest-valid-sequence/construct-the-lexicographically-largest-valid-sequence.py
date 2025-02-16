from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # Initialize the sequence with -1 (empty positions)
        listt = [-1] * ((n - 1) * 2 + 1)
        # Initialize the list of numbers in descending order
        numbers = [i for i in range(n, 0, -1)]

        def largest_form(numbers, curr_pos, listt):
            # If all numbers are placed, return True
            if not numbers:
                return True

            # Skip filled positions
            while curr_pos < len(listt) and listt[curr_pos] != -1:
                curr_pos += 1

            # If we've gone past the end, backtrack
            if curr_pos >= len(listt):
                return False

            # Try placing each number in descending order
            for i in numbers:
                if i == 1:
                    right_pos = curr_pos  # For 1, only one position is needed
                else:
                    right_pos = curr_pos + i  # For numbers > 1, check the second position

                # Check if the placement is valid
                if right_pos < len(listt) and listt[right_pos] == -1:
                    # Place the number
                    listt[curr_pos] = i
                    if i != 1:
                        listt[right_pos] = i

                    # Remove the number from the list of available numbers
                    numbers.remove(i)

                    # Recursively try to place the next number
                    if largest_form(numbers, curr_pos + 1, listt):
                        return True  # If successful, return True

                    # Backtrack: Remove the number and try the next one
                    listt[curr_pos] = -1
                    if i != 1:
                        listt[right_pos] = -1
                    numbers.append(i)  # Reinsert the number into the list
                    numbers.sort(reverse=True)  # Maintain the descending order

            # If no number can be placed, return False
            return False

        # Start the backtracking process
        largest_form(numbers, 0, listt)
        return listt

