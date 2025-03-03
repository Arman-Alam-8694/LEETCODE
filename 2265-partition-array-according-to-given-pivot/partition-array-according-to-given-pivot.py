class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        smaller=0
        larger=0
        equal=0
        result=[0]*n
        for i in nums:
            if i==pivot:
                equal+=1
            elif i<pivot:
                smaller+=1
            else:
                larger+=1
        left=0
        right=smaller
        for i in range(equal):
            result[right]=pivot
            right+=1
        for i in nums:
            if i<pivot:
                result[left]=i
                left+=1
            elif i>pivot:
                result[right]=i
                right+=1

        return result
