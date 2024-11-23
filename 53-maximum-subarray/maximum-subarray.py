class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        maxx=float('-inf')
        n=len(arr)
        summ=0
        for i in range(n):
            summ+=arr[i]
            maxx=max(maxx,summ)
            if summ<0:
                summ=0
           
        return maxx
        