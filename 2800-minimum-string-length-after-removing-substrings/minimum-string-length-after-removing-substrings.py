class Solution:
    def minLength(self, s: str) -> int:
        stack=[]
        for i in s:
            if i=="B" and stack:
                if stack[-1]=="A":
                    stack.pop()
                    continue
            if i=="D" and stack:
                if stack[-1]=="C":
                    stack.pop()
                    continue
            stack.append(i)
        # print(stack)
        return len(stack)

        