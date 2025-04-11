class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result=0
        for i in range(low,high+1):
            n=len(str(i))
            if n&1:
                continue
            else:
                n=n//2
                back=0
                cnt=0
                front=0
                while i!=0:
                    rem=i%10
                    cnt+=1
                    i=i//10
                    if cnt>n:
                        front+=rem
                    else:
                        back+=rem
                if front==back:
                    result+=1 
        return result
                

        