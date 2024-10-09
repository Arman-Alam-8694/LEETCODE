class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count=0
        stack=["dummy"]
        for i in s:
    
            if i==")" and  stack[-1]=="(":
                stack.pop()
                count-=1
            else:
                stack.append(i)
                count+=1
        
        return count
        