class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left=1
        right=sum(candies)//k
        res=0
        def ifPossible(midd,k):
            temp=0
            for i in candies:
                temp+=(i//midd)
                if temp>=k:
                    return True
            return False 
            

        while left<=right:
            mid=(left+right)//2
            # temp=0
            # possible=False
            # for i in candies:
            #     temp+=(i//mid)
            #     if temp>=k:
            #         res=mid
            #         left=mid+1
            #         possible=True
            #         break
            # if not possible:
            #     right=mid-1
            if ifPossible(mid,k):
                res=mid
                left=mid+1
            else:
                right=mid-1
        return res
        