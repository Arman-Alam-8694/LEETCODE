class Solution:
    def robotWithString(self, s: str) -> str:
        position=defaultdict(int)
        

        n=len(s)
        for i in range(n):
            position[s[i]]=i
        last=-1
        result=[]
        stack=[]
        start=0
        for elem in "abcdefghijklmnopqrstuvwxyz":
            while stack and stack[-1]<=elem:
                t=stack.pop()
                result.append(t)
            last=position[elem]
            for i in range(start,last+1):
                if s[i]==elem:
                    result.append(elem)
                else:
                    stack.append(s[i])
            start=i+1
            # print(stack,start)


    
        return "".join(result)

