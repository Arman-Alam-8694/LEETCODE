class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        count=0
        maxx=0
        for i in nums:
            maxx|=i
       
        n=len(nums)
        for i in range(0,2**n):
            cal=0
            for j in range(n):
                if (i&1<<j)!=0:
                    cal|=nums[j]
            if cal==maxx:
                count+=1
        return count