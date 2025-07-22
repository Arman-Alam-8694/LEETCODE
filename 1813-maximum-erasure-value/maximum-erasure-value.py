class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        count={}
        answer=-1
        left=0
        totSum=0
        for right in range(len(nums)):
            while nums[right] in count:
                count[nums[left]]-=1
                totSum-=nums[left]
                if count[nums[left]]==0:
                    del count[nums[left]]
                left+=1
            count[nums[right]]=1
            totSum+=nums[right]
            answer=max(answer,totSum)

    
        return answer

