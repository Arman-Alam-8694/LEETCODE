class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
      
       
        # last_zero=None
        # for i in range(n):
        #     if nums[i]==0 and last_zero is None:
        #         last_zero=i
        #     elif nums[i]!=0 and last_zero is not None:
        #         nums[last_zero]=nums[i]
        #         nums[i]=0
        #         last_zero+=1
        last=0
        for i in range(n):
            if nums[i]!=0:
                nums[last],nums[i]=nums[i],nums[last]
                last+=1
        return nums


        