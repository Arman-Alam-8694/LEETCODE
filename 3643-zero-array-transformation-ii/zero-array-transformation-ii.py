class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        k=0
        rsum=0
        n=len(nums)
        arr=[0]*(n+1)
        for index in range(n):
            while rsum+arr[index]<nums[index]:
                k+=1
                if k>len(queries):
                    return -1
                left,right,val=queries[k-1]
                if right>=index:
                    arr[max(left,index)]+=val
                    arr[right+1]-=val
            rsum+=arr[index]

        return k
        