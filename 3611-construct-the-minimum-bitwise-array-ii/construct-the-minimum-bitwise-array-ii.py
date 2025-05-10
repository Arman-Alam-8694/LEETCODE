class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            if i%2==0:
                res.append(-1)
                continue
            for j in range(0,32):
                if not i&1<<j:
                    res.append((i^1<<j-1))
                    break

        return res



        