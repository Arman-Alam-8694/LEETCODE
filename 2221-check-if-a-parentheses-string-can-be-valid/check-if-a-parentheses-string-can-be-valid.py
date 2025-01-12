class Solution:
    def isValid(self, s: str, locked: str, open_char: str, close_char: str, forward: bool) -> bool:
        n = len(s)
        stack = []
        visited = set()
        indices = range(n) if forward else range(n - 1, -1, -1)

        for i in indices:
            if s[i] == close_char and locked[i] == "1":
                visited.add(i)
                adj_index = i - 1 if forward else i + 1
                if 0 <= adj_index < n and (s[adj_index] == open_char or locked[adj_index] == "0"):
                    adj_next = adj_index - 1 if forward else adj_index + 1
                    if 0 <= adj_next < n and adj_next not in visited:
                        stack.append(adj_next)
                    continue
                elif stack:
                    idx = stack.pop()
                    if 0 <= idx < n and (s[idx] == open_char or locked[idx] == "0"):
                        adj_next = idx - 1 if forward else idx + 1
                        if 0 <= adj_next < n and adj_next not in visited:
                            stack.append(adj_next)
                        continue
                    else:
                        return False
                else:
                    return False
        
        return True

    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        
        # Check forward direction
        if not self.isValid(s, locked, "(", ")", True):
            return False
        
        # Check backward direction
        if not self.isValid(s, locked, ")", "(", False):
            return False
        
        return True
