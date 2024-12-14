class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mapp={}
        for i in nums:
            if i not in mapp:
                mapp[i]=1
            else:
                return i
