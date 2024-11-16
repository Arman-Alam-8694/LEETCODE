class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums
        maxx=-1
        invalid=[]
        n=len(nums)
        for i in range(n-1):
            if nums[i]+1!=nums[i+1]:
                invalid.append(i+1)
        low=0
        result=[]
        # print(invalid)
        for i in range((n-k)+1):
            while  low<len(invalid) and invalid[low]<i+1:
                low+=1
                
            if invalid and low<len(invalid) and i<invalid[low]<(i+k):
                result.append(-1)
            else:
                result.append(nums[(i+k)-1])
        return result
        