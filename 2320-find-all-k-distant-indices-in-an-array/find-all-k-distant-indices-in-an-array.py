class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result=[]
        j=0
        n=len(nums)
        for i in range(n):
            if j<n and abs(j-i)<=k and nums[j]==key:
                result.append(i)
            else:
                if i>j:
                    j+=1
                while j<n and nums[j]!=key:
                    j+=1
                if j<n and abs(j-i)<=k and nums[j]==key:
                    result.append(i)

        return result

        