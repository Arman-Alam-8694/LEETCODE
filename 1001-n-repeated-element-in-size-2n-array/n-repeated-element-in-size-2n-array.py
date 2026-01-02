from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        mapp=defaultdict(int)
        val=-1
        elem=-1
        for i in nums:
            mapp[i]+=1
            if mapp[i]>val:
                val=mapp[i]
                elem=i
        return elem

        