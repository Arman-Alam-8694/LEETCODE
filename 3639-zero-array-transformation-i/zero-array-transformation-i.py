class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n=len(nums)
        counts=[0]*(n+1)
        for start,end in queries:
            counts[start]+=1
            counts[end+1]-=1
        prefix=0
        for i in range(len(counts)-1):
            prefix+=counts[i]
            if prefix<nums[i]:
                return False
        return True

        