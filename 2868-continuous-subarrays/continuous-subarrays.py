class Solution:
    def continuousSubarrays(self, arr: List[int]) -> int:
        left=0
        n=len(arr)
        count=0
        minn=arr[0]
        maxx=arr[0]
        for right in range(n):
            minn=min(minn,arr[right])
            maxx=max(maxx,arr[right])
            if maxx-minn>2:
                size=right-left
                count+=(size*(size+1))//2
                left=right
                minn=arr[right]
                maxx=arr[right]
                while left>0 and abs(arr[right]-arr[left-1])<=2:
                    left-=1
                    minn=min(minn,arr[left])
                    maxx=max(maxx,arr[left])
                if left<right:
                    size=right-left
                    count-=(size*(size+1))//2
        size=right-left+1
        count+=(size*(size+1))//2
        return count
                    

                