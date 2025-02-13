class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        op=0
        heapify(nums)
        while len(nums)>=2 and nums[0]<k:
            op+=1
            a=heappop(nums)
            b=heappop(nums)
            if a>b:
                part1=a
                part2=b*2
            else:
                part2=b
                part1=a*2
            heappush(nums,part1+part2)

        

        return op