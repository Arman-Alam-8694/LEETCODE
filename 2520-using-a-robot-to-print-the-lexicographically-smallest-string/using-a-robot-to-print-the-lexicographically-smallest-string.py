class Solution:
    def robotWithString(self, s: str) -> str:
        position=defaultdict(list)
        n=len(s)
        last=-1
        for i in "abcdefghijklmnopqrstuvwxyz":
            for j in range(n):
                if last<j and s[j]==i:
                    position[i].append(j)
                    last=j
        # print(position)
        result=[]
        stack=[]
        start=0
        for k in "abcdefghijklmnopqrstuvwxyz":
            elem=k
            pos=position[elem]
            while stack and stack[-1]<=elem:
                t=stack.pop()
                result.append(t)
            stack_pos=0
            if pos:
                for i in range(start,pos[-1]+1):
                    if pos[stack_pos]==i:
                        result.append(elem)
                        stack_pos+=1
                    else:
                        stack.append(s[i])
                start=i+1

    
        return "".join(result)

