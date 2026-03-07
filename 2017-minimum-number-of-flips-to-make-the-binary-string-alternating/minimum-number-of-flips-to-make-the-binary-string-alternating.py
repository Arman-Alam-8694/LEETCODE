class Solution:
    def minFlips(self, s: str) -> int:
        zero=[0,0]
        one=[0,0]
        n=len(s)
        for i in range(n):
            if s[i]!="0":
                zero[i%2]+=1
            else:
                one[i%2]+=1
                
        print(zero)
        print(one)
        res=float("inf")
        res=min(zero[0]+one[1],one[0]+zero[1])
        for i in range(n):
            curr=s[i]
            if curr=="0":
                one[0]-=1
            else:
                zero[0]-=1
            zero[0],zero[1]=zero[1],zero[0]
            one[0],one[1]=one[1],one[0]

            if curr=="0":
                one[(n-1)%2]+=1
            else:
                zero[(n-1)%2]+=1
            res=min(res,zero[0]+one[1],one[0]+zero[1])

        return res




        