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
        new=sorted(position.keys(),key=lambda x:x)
        # print(new)
        for elem in new:
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
        return "".join(result)

