class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        mapp=Counter(nums)
        ndistinct=set()
        n=len(nums)
        for k,v in mapp.items():
            if v>1:
                ndistinct.add(k)

        if len(ndistinct)==0:
            return 0
        if n<=3:
            return 1
        cnt=0
        steps=0
        right=-1
        # print(ndistinct)
        # print(mapp)
        for i in nums:
            right+=1
            cnt+=1
            mapp[i]-=1
            if mapp[i]==1:
                # print(i)
                # print(mapp)
                ndistinct.remove(i)
            if cnt==3:
                steps+=1
                if len(ndistinct)==0:
                    return steps
                if n-right<=3:
                    return steps+1
                cnt=0
        return steps