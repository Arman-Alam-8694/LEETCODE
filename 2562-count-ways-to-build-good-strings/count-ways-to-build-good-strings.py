class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7

        # Memoization dictionary
        memo = {}

        def recur(size):
            if size > high:  # Base case: size exceeds the high limit
                return 0
            if size in memo:  # Check if result is already computed
                return memo[size]

            # Initialize count for this size
            count = 0
            if low <= size <= high:  # If size is within the valid range, count it
                count += 1
            
            # Recursive calls for adding `zero` and `one`
            count += recur(size + zero)
            count += recur(size + one)
            count %= MOD  # Take modulo to avoid overflow

            # Store result in memo and return it
            memo[size] = count
            return count

        # Start recursion with size 0
        return recur(0)
