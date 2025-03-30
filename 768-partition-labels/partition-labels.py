class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        seen={}
        res=[]
        stack=[-1]
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]]=i
                stack.append(i)
            else:
                while stack[-1]>=seen[s[i]]:
                    stack.pop()
                stack.append(i)

        for i in range(len(stack)-1):
            res.append(stack[i+1]-stack[i])
        return res


        