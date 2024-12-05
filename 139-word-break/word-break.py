from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        queue = deque([0])  # Start with the first index
        memo = {}  # Memoization to store results for each index
        lookup = set(wordDict)  # Set of valid words
        n = len(s)
        
        while queue:
            idx = queue.popleft()
            
            # If we have reached the end of the string, return True
            if idx == n:
                return True
            
            # Memoization check
            if idx in memo:
                if memo[idx] == False:
                    continue  # Skip if this index is known to lead to no solution
            
            # Try all possible substrings starting from this index
            for i in range(idx + 1, n + 1):
                if s[idx:i] in lookup:
                    queue.append(i)  # Add the next valid index to the queue

            # Memoize this index: if no valid continuation from this point, mark as False
            if not queue or (idx not in memo):
                memo[idx] = False  # Mark as False if no valid path forward

        return False
