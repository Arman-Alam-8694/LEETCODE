class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        count={}
        count=[0]*10001
        answer=-1
        left=0
        totSum=0
        for right in range(len(nums)):
            while count[nums[right]]==1:
                count[nums[left]]-=1
                totSum-=nums[left]
                left+=1
            count[nums[right]]+=1
            totSum+=nums[right]
            answer=max(answer,totSum)

    
        return answer

