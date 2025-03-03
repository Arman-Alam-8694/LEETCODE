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
        equal=smaller
        right=n-larger
        for i in nums:
            if i<pivot:
                result[left]=i
                left+=1
            elif i>pivot:
                result[right]=i
                right+=1
            else:
                result[equal]=i
                equal+=1

        return result

        # small=[]
        # n=len(nums)
        # equal=[]
        # large=[]
        # for i in nums:
        #     if i<pivot:
        #         small.append(i)
        #     elif i>pivot:
        #         large.append(i)
        #     else:
        #         equal.append(i)
        # return small+equal+large
