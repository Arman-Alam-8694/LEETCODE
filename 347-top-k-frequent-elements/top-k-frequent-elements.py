from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp=Counter(nums)
        new =sorted(mapp.items(),key=lambda x:x[1],reverse=True)
        result=[]
        for i in range(k):
            result.append(new[i][0])
        return result    