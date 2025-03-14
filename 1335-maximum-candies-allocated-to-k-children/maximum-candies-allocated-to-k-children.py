class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left=0
        right=max(candies)
        def ifPossible(midd,k):
            temp=k
            for i in candies:
                temp-=(i//midd)
                if temp<=0:
                    return True
            return False 
            

        while left<=right:
            mid=(left+right)//2
            if mid==0 or ifPossible(mid,k):
                left=mid+1
            else:
                right=mid-1
        return right
        