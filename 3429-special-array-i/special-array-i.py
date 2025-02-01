class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # n=len(nums)
        # if nums[0]&1:
        #     prev="even"
        # else: prev="odd"
        # for  i in range(n):
        #     if nums[i]&1:
        #         if prev=="even":
        #             prev='odd'
        #         else:
        #             return False
        #     else:
        #         if prev=="odd":
        #             prev='even'
        #         else:
        #             return False
        # return True


        # n=len(nums)
        # for i in range(n-1):
        #     if nums[i]&1==nums[i+1]&1:
        #         return False
        # return True


        return False if any(nums[i]&1==nums[i+1]&1 for i in range(len(nums)-1)) else True
                


        