from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        mapp={}
        for i in nums:
            if i in mapp:
                return i
            mapp[i]=1
        

        