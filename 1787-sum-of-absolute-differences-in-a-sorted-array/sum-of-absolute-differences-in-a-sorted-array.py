class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        summ=sum(nums)
        n=len(nums)
        result=[]
        prefix_sum=0
        for i in range(n):
            tright=summ-prefix_sum
            right=tright-(nums[i]*(n-i))
            left=(nums[i]*(i-0))-prefix_sum
            prefix_sum+=nums[i]
            result.append(left+right)
        return result



