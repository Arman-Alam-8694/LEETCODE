class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lookup=set(nums)
        size=1
        for i in lookup:
            if (i-1 not in lookup) and (i+1 in lookup):
                start=i
                count=0
                while True:
                    if start in lookup:
                        count+=1
                    else:
                        size=max(size,count)
                        break
                    start+=1
        return size
