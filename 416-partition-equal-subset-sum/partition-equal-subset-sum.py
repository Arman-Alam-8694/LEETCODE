class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        total=sum(nums)
        if total&1:
            return False
        totall=total//2
        map={}
        def subset(sum,start,n,totall):
            if (sum,start) in map:
                return map[(sum,start)]
          
            if sum>totall:
                return False
            if sum==totall:
                return True
            if start>=n:
                return False
            result=subset(sum+nums[start],start+1,n,totall) or subset(sum,start+1,n,totall)
            map[(sum,start)]=result
            return map[(sum,start)]
            

        return subset(0,0,n,totall)
       


        