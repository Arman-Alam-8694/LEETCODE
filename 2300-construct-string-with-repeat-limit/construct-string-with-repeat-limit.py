from collections import Counter,deque
class Solution:
    def repeatLimitedString(self, s: str, k: int) -> str:
        counts=Counter(s)
        # n=len(count)
        # check=[[]*n]
        ch=deque(sorted(counts.items(),key=lambda x:x[0],reverse=True))
        check=[]
        for i in ch:
            check.append(list(i))
        # print(check)
        prev=0
        curr=0
        answer=[]
        while True:
            # print(check)
            if curr>=len(check):
                return "".join(answer)
           
            while check[curr][1]==0:
                curr+=1
                if curr>=len(check):
                    return "".join(answer)
            while check[prev][1]==0:
                prev+=1
                if curr>=len(check):
                    return "".join(answer)
            
            if prev==curr:
                if check[curr][0]=="b":
                    print(check)
                answer.extend([check[curr][0]]*min(check[curr][1],k))
                check[curr][1]-=min(check[curr][1],k)
                if check[curr][1]==0:
                    prev+=1
                    curr+=1
                else:
                    curr+=1
            elif prev!=curr:
                answer.append(check[curr][0])
                check[curr][1]-=1
                curr=prev



