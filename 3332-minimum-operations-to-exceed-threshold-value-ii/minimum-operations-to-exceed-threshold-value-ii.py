class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        op=0
        heapify(nums)
        while len(nums)>=2 and nums[0]<k:
            op+=1
            a=heappop(nums)
            b=heappop(nums)
            heappush(nums,a*2+b)
        return op