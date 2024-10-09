class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count=0
        stack=[]
        for i in s:
            if stack:
                if i=="(" and stack[-1]=="(" or i=="(" and stack[-1]==")" :
                    stack.append(i)
                    count+=1
                elif i==")" and stack[-1]==")":
                    stack.append(i)
                    count+=1
                else:
                    stack.pop()
                    count-=1
            else:
                stack.append(i)
                count+=1
        return count
        