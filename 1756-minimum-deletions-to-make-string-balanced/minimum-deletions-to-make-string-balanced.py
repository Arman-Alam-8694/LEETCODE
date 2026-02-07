class Solution:
    def minimumDeletions(self, s: str) -> int:
      
        stack=[]
        pop=0
        for i in range(len(s)):
            if stack and stack[-1]=="b" and s[i]=="a":
                pop+=1
                stack.pop()
            else:
                stack.append(s[i])
       
        return pop
            
        