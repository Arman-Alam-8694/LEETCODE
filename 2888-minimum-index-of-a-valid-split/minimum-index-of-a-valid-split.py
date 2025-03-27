class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dictt={}
        item=0
        maxx=float("-inf")
        for i in nums:
            if i not in dictt:
                dictt[i]=0
            dictt[i]+=1
            maxx=max(maxx,dictt[i])
            if dictt[i]==maxx:
                item=i

        # item=0

        # for k,v in dictt.items():
        #     if v==maxx:
        #         item=k
        #         break
        n=len(nums)
        run=0
        for i in range(len(nums)-1):
            if nums[i]==item:
                run+=1
                maxx-=1
            if run*2>(i+1) and (n-1)-i<maxx*2:
                return i
        return -1
 
            
        