class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n=len(arr)
        maxx=0
        indexes={j:i for i,j in enumerate(arr)}
        mapp={}  
        # def dp(prev,prev1,length):
        #     if (prev,prev1) in mapp:
        #         return mapp[(prev,prev1)]
        #     temp=arr[prev]+arr[prev1]
        #     if temp in indexes:
        #         i=indexes[temp]
        #         ansss=dp(i,prev,length+1)
        #         mapp[(prev,prev1)]=ansss
        #         return ansss
        #     return length


        # for i in range(n):
        #     for j in range(:
        #         ans=dp(j,i,2)
        #         maxx=max(maxx,0 if ans==2 else ans )
        # return maxx

        for j in range(n):
            for i in range(j):
                prev=arr[j]-arr[i]
                if prev in indexes and indexes[prev]<i:
                    k=indexes[prev]
                    mapp[(i,j)]=mapp.get((k,i),2)+1
                    maxx=max(maxx,mapp[(i,j)])
        return maxx
            
            
            
                








        