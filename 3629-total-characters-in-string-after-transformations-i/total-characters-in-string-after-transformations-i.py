class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        res=0
        MOD=10**9+7
        # for i in s:
        #     req=ord("z")-ord(i)+1
        #     # print(req)
        #     if req>t:
        #         res+=1
        #     else:
        #         rem=t-req
        #         res+=2
        #         #here a,b is formed
        #         rounds,fora=divmod(rem,25)
        #         if rounds>0 and fora>0:
        #             res+=2*rounds
        #         elif rounds>0 and fora==0:
        #             res+=2*rounds-1

        #     # print(req)
     
        temp=[0]*26
        for i in s:
            temp[ord(i)-ord("a")]+=1
        for rounds in range(t):
            next=[0]*26
            for i in range(0,26):
                if temp[i]>0:
                    if i==25:
                        next[0]+=temp[i]
                        next[1]+=temp[i]
                        
                    else:
                        next[i+1]+=temp[i]
            # print(next)
            temp=next
        return sum(temp)%MOD



