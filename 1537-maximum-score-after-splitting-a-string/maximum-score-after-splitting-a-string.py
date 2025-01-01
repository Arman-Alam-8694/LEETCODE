class Solution:
    def maxScore(self, s: str) -> int:
        # dictt={}
        # n=len(s)
        # zero=0
        # ones=0
        # for i in range(n):
        #     dictt[i]=[0,0]
        #     if s[i]=="0":
        #         zero+=1
        #     else:
        #         ones+=1
        #     dictt[i][1]=ones
        #     dictt[i][0]=zero
        # maxx=float("-inf")
       
    
        # for i in range(n-1):
        #     remone=dictt[n-1][1]-dictt[i][1]
        #     maxx=max(maxx,remone+dictt[i][0])
        # return maxx

        maxx=float('-inf')
        ones=0
        zero=0
        n=len(s)
        for i in s:
            if i=="1":
                ones+=1
        for i in range(n-1):
            zero+=1 if s[i]=="0" else 0
            ones+=0 if s[i]=="0" else -1
            maxx=max(maxx,zero+ones)
        return maxx
        