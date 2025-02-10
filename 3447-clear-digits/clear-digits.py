class Solution:
    def clearDigits(self, s: str) -> str:
        n=len(s)
        stack=[]
        for i in range(n):
            if s[i].isdigit():
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
            
        