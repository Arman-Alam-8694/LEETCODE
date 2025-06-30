class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        count=0
        answer=0
        # left,right=0,n-1
        # while left<=right:
        #     while right>=0 and nums[right]-nums[left]!=1:
        #         right-=1
        #     result=max(result,right-left+1)
        #     left+=1

        dictt=defaultdict(int)
        for right in range(n):
            if nums[right]-1 in dictt:
                idx=dictt[nums[right]-1]
                answer=max(answer,right-idx+1)
            if nums[right] not in dictt:
                dictt[nums[right]]=right
        return answer

        # return result

        