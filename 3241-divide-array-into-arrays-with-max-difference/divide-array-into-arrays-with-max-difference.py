class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result=[]
        temp=[]
        for i in nums:
            temp.append(i)
            if temp and temp[-1]-temp[0]>k:
                return []
            if len(temp)==3:
                result.append(temp[:])
                temp=[]
        return result