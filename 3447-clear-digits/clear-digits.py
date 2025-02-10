class Solution:
    def clearDigits(self, s: str) -> str:
        n=len(s)
        stack=[]
        for i in range(n):
            if s[i].isdigit():
                if stack:
                    stack.pop()
                else:
                    res.append(s[i])
            else:
                stack.append(s[i])
        return "".join(stack)
            
        