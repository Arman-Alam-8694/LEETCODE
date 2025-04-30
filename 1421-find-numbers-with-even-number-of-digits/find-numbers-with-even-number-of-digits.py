class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even=0
        for n in nums:
            if not len(str(n))&1:
                even+=1

        return even
        