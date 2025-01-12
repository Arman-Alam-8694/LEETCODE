class Solution:
    def isValid(self, s: str, locked: str, open_char: str, close_char: str) -> bool:
        n = len(s)
        stack = []
        visited = set()
        
        for i in range(n):
            if s[i] == close_char and locked[i] == "1":
                visited.add(i)
                if i - 1 >= 0 and (s[i - 1] == open_char or locked[i - 1] == "0"):
                    if i - 2 not in visited:
                        stack.append(i - 2)
                    continue
                elif stack:
                    idx = stack.pop()
                    if idx >= 0 and (s[idx] == open_char or locked[idx] == "0"):
                        if idx - 1 not in visited:
                            stack.append(idx - 1)
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
        
      
        if not self.isValid(s, locked, "(", ")"):
            return False
     
        reversed_s = s[::-1]
        reversed_locked = locked[::-1]
        
     
        if not self.isValid(reversed_s, reversed_locked, ")", "("):
            return False
        
        return True
