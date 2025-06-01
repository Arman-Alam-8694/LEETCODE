class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result=0
        for i in range(min(limit,n)+1):
            rem_sum=n-i
            if limit*2>=rem_sum:
                # sec=min(limit,rem_sum)
                # last=min(limit,rem_sum-sec)
                # if sec==last:
                #     result+=1
                # if sec!=last:
                #     result+=2
                # x,y=divmod((sec-last),2)
                # if x!=0:
                #     result+=x*2
                #     if y==0:
                #         result-=1
                max_b=min(limit,rem_sum)
                min_b=max(0,rem_sum-limit)
                result+=max_b-min_b+1
        return result

        