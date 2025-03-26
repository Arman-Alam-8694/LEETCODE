class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        def check(midd,array):
            # print(midd)
            cnt=0
            for y in array:
                if y==midd:
                    continue
                temp=abs(y-midd)
                # print("here",temp,temp%x)
                if temp%x==0:

                    cnt+=(temp//x)
                else:
                    return -1
            return cnt
        array=[]
        m=len(grid)
        n=len(grid[0])
        odd,even=0,0
        for i in range(m):
            for j in range(n):
                if grid[i][j]&1:
                    odd+=1
                else:
                    even+=1
                array.append(grid[i][j])
        array.sort()
        # array.pop(0)
        # array.pop()
        # print(array)
        if odd!=0 and odd!=m*n and x!=1:
            if not x&1:
                return -1

        start=0
        end=len(array)-1
        mini=float("inf")
        while start<=end:
            mid=(start+end)//2
            res=check(array[mid],array)
            # print(res)
            if res==-1:
                start=mid+1

            else:
                if res<mini:
                    mini=res

                    end=mid-1
                else:
                    start=mid+1
        return mini if mini!=float("inf") else -1
        