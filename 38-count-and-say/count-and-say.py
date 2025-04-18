class Solution:
    def countAndSay(self, n: int) -> str:
        def recur(time,num):
            if time==n:
                return num
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
            # print(temp,times)
            temp+=str(times)
            temp+=i
            return recur(time+1,temp)
        return recur(1,"1")
                
            


        