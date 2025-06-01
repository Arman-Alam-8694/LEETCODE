class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result=0
        for i in range(min(limit,n)+1):
            rem_sum=n-i
            # print(rem_sum)
            if limit*2>=rem_sum:
                # print("here")
                sec=min(limit,rem_sum)
                last=min(limit,rem_sum-sec)
                # print(i,sec,last)
                if sec==last:
                    result+=1
                if sec!=last:
                    result+=2
                x,y=divmod((sec-last),2)
                if x!=0:
                    result+=x*2
                    if y==0:
                        result-=1
        return result
    # 0 0 3
    # 0 1 2
    # 0 2 1


        