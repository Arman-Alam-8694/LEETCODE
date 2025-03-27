class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dictt={}
        maxx=float("-inf")
        for i in nums:
            if i not in dictt:
                dictt[i]=0
            dictt[i]+=1
            maxx=max(maxx,dictt[i])
        item=0

        for k,v in dictt.items():
            if v==maxx:
                item=k
        n=len(nums)
        run=0
        for i in range(len(nums)-1):
            if nums[i]==item:
                run+=1
                maxx-=1
            if run*2>(i+1):
                if (n-1)-i<maxx*2:
                    return i
        return -1
 
            
        