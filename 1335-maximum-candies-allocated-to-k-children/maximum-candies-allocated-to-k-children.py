class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left=0
        right=sum(candies)
        def ifPossible(midd,k):
            temp=k
            # print(midd)
            for i in candies:
                temp-=(i//midd)
                # print(temp)
                if temp<=0:
                    # print("true")
                    return True
            return False 
            

        while left<=right:
            mid=(left+right)//2
            if mid==0:
                left=mid+1

            elif ifPossible(mid,k):
                # print('here',mid)
                left=mid+1
            else:
                right=mid-1
        return right
        