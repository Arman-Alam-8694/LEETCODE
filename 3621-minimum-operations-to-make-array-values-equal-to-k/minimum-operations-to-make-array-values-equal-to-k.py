class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # nums.sort(reverse=True)
        # steps=0
        # n=len(nums)
        # temp=nums[0]
        # for i in range(n):
        #     if nums[i]<k:
        #         return -1
        #     if nums[i]!=temp:
        #         steps+=1
        #         temp=nums[i]
        # return steps+1 if temp>k else steps

        # sett=set()
        # smallest=float("inf")
        # for i in nums:
        #     if i<k:
        #         return -1
        #     sett.add(i)
        # # print(smallest)
        # return len(sett)-1 if k in sett else len(sett)
        
        return -1 if min(nums)<k else len(set(filter(lambda n:n>k,nums)))

        