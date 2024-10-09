class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        result=""
        openn=0
        close=0
        for i in s:
            if (stack and openn==close) and (i=="(" and stack[-1]==")"):
                stack.pop()
                stack.pop(0)
                string="".join(stack)
                print(string)
                result+=string
                stack=[]
                stack.append(i)
                close=0
                openn=1
            else:
                stack.append(i)
                if i=="(":
                    openn+=1
                else:
                    close+=1

        if stack:
            stack.pop()
            stack.pop(0)
        result+="".join(stack)

        return result
        