class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        def bins(number,map_temp):

            left=0
            right=len(map_temp)-1
            while left<=right:
                mid=(left+right)//2
                if map_temp[mid][0]>number:
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
        map_temp=[]
        for i,j in mapp.items():
            map_temp.append((i,j))
        
        result=[]
        for i in queries:
            if i in mapp:
                result.append(mapp[i])
            else:
                idx=bins(i,map_temp)
                if idx==0:
                    result.append(0)
                else:
                    result.append(map_temp[idx-1][1])
        return result

        