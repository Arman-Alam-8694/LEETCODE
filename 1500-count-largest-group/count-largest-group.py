class Solution:
    def countLargestGroup(self, n: int) -> int:
        mapp=[0]*37
        largest=0
        large_count=0
        for num in range(1,n+1):
            summ=0
            while num!=0:
                summ+=num%10
                num//=10
            mapp[summ]+=1
            if mapp[summ]>largest:
                largest=mapp[summ]
                large_count=1
            elif mapp[summ]==largest:
                # print(summ)
                large_count+=1
        return large_count
        
            
