class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=0
        nleft=0
        answer=0
        for i in nums:
            if i==0:
                answer=max(answer,left+nleft)
                left=nleft
                nleft=0
            else:
                nleft+=1
        answer=max(answer,left+nleft)
        return answer if answer!=len(nums) else answer-1

        