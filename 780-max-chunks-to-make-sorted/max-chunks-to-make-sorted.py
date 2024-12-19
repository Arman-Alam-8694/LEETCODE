class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        minn=None
        maxx=None
        chunks=0
        n=len(arr)
        quant=[0]*n
        for i in range(n):
            if not minn and not maxx:
                minn=arr[i]
                maxx=arr[i]
                chunks+=1
                quant[i]=chunks
                
        
            elif (minn-1<=arr[i]<=maxx-1):
                minn=min(minn,arr[i])
                maxx=max(maxx,arr[i])
                continue
            elif maxx+1==arr[i]:
                chunks+=1
                minn=arr[i]
                maxx=arr[i]
                quant[i]=chunks
            elif arr[i]>maxx:
                minn=arr[i]
                maxx=arr[i]
                chunks+=1
                quant[i]=chunks

            else:
                comp=arr[i]
                till=i
                for i in range(comp,-1,-1):
                    if arr[i]>comp:
                        last=i
                        chunks=quant[i]
                for j in range(last,till+1):
                    minn=min(minn,arr[j])
                    maxx=max(maxx,arr[j])
                    quant[j]=chunks
        # print(quant)
        return chunks
            
        