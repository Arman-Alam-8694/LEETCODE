class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dictt={}
        item=0
        cnt=0
        for i in nums:
            if cnt==0:
                item=i
            if item==i:
                cnt+=1
            else:
                cnt-=1
        maxx=nums.count(item)

        # item=0

        # for k,v in dictt.items():
        #     if v==maxx:
        #         item=k
        #         break
        n=len(nums)
        # if n == maxx * 2 - 1:
        #     return -1
        run=0
        for i in range(len(nums)-1):
            if nums[i]==item:
                run+=1
                maxx-=1
            if run*2>(i+1) and (n-1)-i<maxx*2:
                return i
        return -1
 
            
        