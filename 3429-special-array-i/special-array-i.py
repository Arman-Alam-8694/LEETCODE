class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n=len(nums)
        if nums[0]&1:
            prev="even"
        else: prev="odd"
        for  i in range(n):
            if nums[i]&1:
                if prev=="even":
                    prev='odd'
                else:
                    return False
            else:
                if prev=="odd":
                    prev='even'
                else:
                    return False
        return True
                


        