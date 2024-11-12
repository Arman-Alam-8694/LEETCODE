class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        def bins(number,items):
            left=0
            right=len(items)-1
            while left<=right:
                mid=(left+right)//2
                if items[mid][0]>number:
                    right=mid-1
                else:
                    left=mid+1
            return left
        mapp={}
        items.sort()
        maxx=float('-inf')
        for i,j in items:
           
            if i not in mapp:
                maxx=max(maxx,j)
                mapp[i]=maxx
            else:
                maxx=max(maxx,j)
                mapp[i]=maxx
        
        result=[]
        for i in queries:
            if i in mapp:
                result.append(mapp[i])
            else:
                idx=bins(i,items)

                if idx==0:
                    result.append(0)
                else:
                    value=items[idx-1][0]
                    result.append(mapp[value])
        return result

        