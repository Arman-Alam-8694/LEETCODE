class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        result=float("-inf")
        n=len(nums)
        listt=[(nums[i],i) for i in range(n)]
        listt.sort()
        new=listt[n-k:]
        new.sort(key=lambda x:x[1])
        answer=[]
        for i,j in new:
            answer.append(i)
        return answer