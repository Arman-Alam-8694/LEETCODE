class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        counts=[0]*51
        for i in nums:
            counts[i]+=1
        start=1
        top=[]
        while start<51:
            while counts[start]!=0 and len(top)!=3:
                top.append(start)
                counts[start]-=1
            if len(top)==3:
                break
            start+=1
     
        result=0
        left=2
        curr=nums[0]
        if curr in top:
            return sum(top)
        else:
            return curr+top[0]+top[1]

        
        