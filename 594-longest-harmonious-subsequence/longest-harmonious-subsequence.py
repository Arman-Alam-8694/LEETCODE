class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        count=0
        answer=0
        # left,right=0,n-1
        # while left<=right:
        #     while right>=0 and nums[right]-nums[left]!=1:
        #         right-=1
        #     result=max(result,right-left+1)
        #     left+=1

        dictt=defaultdict(int)
        left=0
        for right in range(n):
            while left<right and nums[right]-1>nums[left]:
                left+=1
            if nums[left]==nums[right]-1:
                answer=max(answer,right-left+1)
          
        return answer

        # return result

        