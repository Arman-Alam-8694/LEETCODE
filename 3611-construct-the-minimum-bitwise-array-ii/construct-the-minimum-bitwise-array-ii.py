class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result=[]
        for num in nums:
            if not num&1:
                result.append(-1)
                continue
            for j in range(1,31):
                if (num&(1<<j)):
                    continue
                result.append(num^(1<<j-1))
                break
        return result