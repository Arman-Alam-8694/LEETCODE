class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        def binsearch(search,number):
            left=0
            right=len(search)-1
            while left<=right:
                mid=(left+right)//2
                if search[mid]<number:
                    left=mid+1
                else:
                    right=mid-1
            return left
        perfect_sort=0
        first=None
        n=len(arr)
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                if not first:
                    first=i+1
                perfect_sort=i+1
        search=arr[perfect_sort:]
        count=float('inf')

        # print(first,perfect_sort)
        if first==0:
            ind=binsearch(serach,arr[first])
            ind=perfect_sort+ind
            return (ind-first)-1
        if first:
            first-=1
        while first!=None and first>=0:
            ind=binsearch(search,arr[first])
            ind=perfect_sort+ind
            if first==0:
                count=min(count,(ind-first)-1,(perfect_sort-first))

                first-=1
                continue
            count=min(count,(ind-first)-1)
            print(first,ind,count)
            first-=1

        return count if count!=float('inf') else 0
        