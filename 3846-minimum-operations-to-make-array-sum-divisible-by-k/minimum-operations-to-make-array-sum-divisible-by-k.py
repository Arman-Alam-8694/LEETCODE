class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        summ=sum(nums)
        return summ%k
        