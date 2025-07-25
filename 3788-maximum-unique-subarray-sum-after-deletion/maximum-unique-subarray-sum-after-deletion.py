class Solution:
    def maxSum(self, nums: List[int]) -> int:
        big_neg=float("-inf")
        found=False
        for i in nums:
            if i>=0:
                found=True
                break
        if found:
            listt=[0]*101
            for i in nums:
                if i>0 and listt[i]==0:
                    listt[i]=i
            
            return sum(listt)
        else:
            neg=float("-inf")
            for i in nums:
                if i<0:
                    neg=max(neg,i)
            return neg

        