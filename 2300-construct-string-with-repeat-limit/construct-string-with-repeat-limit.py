from collections import Counter
class Solution:
    def repeatLimitedString(self, s: str, k: int) -> str:
        counts=Counter(s)
        check=sorted(counts.items(),key=lambda x:x[0],reverse=True)
        # check=[]
        # for i in ch:
        #     check.append(list(i))
        prev=0
        curr=0
        answer=[]
        while True:
            if curr>=len(check):
                return "".join(answer)
            while check[curr][1]==0:
                curr+=1
                if curr>=len(check):
                   
                    return "".join(answer)
            if check[prev][1]==0:
                prev=curr
            if prev==curr:
                char,val=check[curr]
                answer.append(char*min(val,k))
                val-=min(val,k)
                check[curr]=(char,val)
                if check[curr][1]==0:
                    prev+=1
                    curr+=1
                else:
                    curr+=1
            elif prev!=curr:
                char,val=check[curr]
                answer.append(check[curr][0])
            
                check[curr]=(char,val-1)
                curr=prev



