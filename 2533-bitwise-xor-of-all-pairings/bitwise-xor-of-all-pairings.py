class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        a=len(nums1)
        b=len(nums2)
        bitmask=0
        if b&1:
            for i in nums1:
                bitmask^=i
        if a&1:
            for i in nums2:
                bitmask^=i
        return bitmask        