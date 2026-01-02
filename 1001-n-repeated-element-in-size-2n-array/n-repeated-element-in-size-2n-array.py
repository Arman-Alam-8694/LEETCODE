from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        mapp=Counter(nums)
        print(mapp)
        val=-1
        elem=-1
        for i,j in mapp.items():
            if j>val:
                val=j
                elem=i
        return elem

        