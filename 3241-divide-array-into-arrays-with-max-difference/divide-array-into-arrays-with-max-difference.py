class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result=[[]]
        temp=[]
        for i in nums:
            result[-1].append(i)
            if result[-1] and result[-1][-1]-result[-1][0]>k:
                return []
            if len(result[-1])==3:
                result.append([])
        result.pop()
        return result