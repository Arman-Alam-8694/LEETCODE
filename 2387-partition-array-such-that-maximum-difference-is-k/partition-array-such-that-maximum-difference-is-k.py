class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        answer=0
        nums.sort()
        smallest=nums[0]
        for i in nums:
            if i-smallest>k:
                answer+=1
                smallest=i

        return answer+1        
            

        