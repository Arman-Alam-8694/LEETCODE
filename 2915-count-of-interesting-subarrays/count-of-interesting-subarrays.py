class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        mapp=defaultdict(int)
        mapp[0]=1
        prefix=0
        res=0
        for n in nums:
            prefix+=1 if n%modulo==k else 0
            res+=mapp[(prefix-k)%modulo]
            mapp[prefix%modulo]+=1
        return res
        