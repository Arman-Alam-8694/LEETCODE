class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mapp=defaultdict(list)
        n=len(nums)
        for i in range(n):
            num=nums[i]
            temp=0
            while num!=0:
                temp+=num%10
                num//=10
            mapp[temp].append(nums[i])

        maxx=-1
        for key,val in mapp.items():
            # print(val)
            if len(val)>=2:
                a=max(val)
                val.remove(a)
                b=max(val)
                maxx=max(maxx,a+b)
        return maxx
        