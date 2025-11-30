class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n=len(nums)
        parray=[0]*(n+1)
        for i in range(n):
            parray[i+1]=parray[i]+nums[i]
        total=parray[n]
        if total%p==0:
            return 0
        mapp={}
        maxx=0
        for i in range(n):
            second=(total-parray[i])%p
            first=(total-second)%p
            slen=n-(i)
            flen=n-slen
            temp=p-second
            print(i)
            print(second,first)
            print(slen,flen)
            if first==0:
                maxx=max(maxx,flen)
            if second==0 and 0 in mapp:
                maxx=max(maxx,mapp[0]+slen)
            if temp in mapp:
                maxx=max(maxx,mapp[temp]+slen)
    
            if first in mapp:
                mapp[first]=max(mapp[first],flen)
            else:
                mapp[first]=flen

        return n-maxx if maxx!=0 else -1



        