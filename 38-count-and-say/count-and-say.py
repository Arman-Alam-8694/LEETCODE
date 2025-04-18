class Solution:
    def countAndSay(self, n: int) -> str:
        num="1"
        for i in range(n-1):
            temp=""
            times=1
            prev=None
            for i in num:
                if prev is None:
                    prev=i
                elif prev==i:
                    times+=1
                else:
                    temp+=str(times)
                    temp+=prev
                    prev=i
                    times=1
         
            temp+=str(times)
            temp+=i
            num=temp
            n-=1
        return num
                
            


        