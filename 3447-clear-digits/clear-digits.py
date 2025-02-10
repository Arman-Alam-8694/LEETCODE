class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in s:
            if i.isdigit()==False:
                stack.append(i)
            else:
                stack.pop()
        res=''.join(stack)
        return res
        
