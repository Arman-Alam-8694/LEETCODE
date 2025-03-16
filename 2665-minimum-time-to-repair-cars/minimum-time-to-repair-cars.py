class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left=1
        right=max(ranks)*cars*cars
        n=len(ranks)
        lookup=[0]*101
        for i in ranks:
            lookup[i]+=1
        def isPossible(mid):
            count=0
            for i in range(1,len(lookup)):
                count+=(int(math.sqrt(mid//i))*lookup[i])
                if count>=cars:
                    return True
            return False

  
        while left<=right:
            mid=(left+right)//2
            if isPossible(mid):
                right=mid-1
            else:
                left=mid+1
        return left