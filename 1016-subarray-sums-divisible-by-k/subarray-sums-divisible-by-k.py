class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder=[0]*k
        remainder[0]=1
        res=0
        prefix=0
        for num in nums:
            prefix+=num
            remain=prefix%k
            res+=remainder[remain]
            remainder[remain]+=1
        return res

        