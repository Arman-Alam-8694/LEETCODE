class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        prefix=[]
        p=0
        for i in nums:
            p+=i
            prefix.append(p)
        for i in range(1,len(nums)):
            right=prefix[-1]-prefix[i-1]
            left=prefix[i-1]
            if (abs(left-right))%2==0:
                count+=1

        return count
        