class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxx=0
        n=len(nums)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    temp=(nums[i]-nums[j])*nums[k]
                    maxx=max(maxx,temp)
        return 0 if maxx<0 else maxx

        