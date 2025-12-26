class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        happiness.sort(reverse=True)
        r=0
        ans=0
        for i in happiness:
            if (i-r)<=0:
                return ans
            ans+=(i-r)
            r+=1
            k-=1
            if k==0:
                return ans
        return ans

    

        