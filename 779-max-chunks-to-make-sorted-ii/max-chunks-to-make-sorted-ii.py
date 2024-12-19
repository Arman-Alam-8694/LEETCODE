class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        minn=None
        maxx=None
        chunks=0
        n=len(arr)
        quant=[0]*n
        seen=set()
        for i in range(n):
           
            if not minn and not maxx:
                minn=arr[i]
                maxx=arr[i]
                chunks+=1
                quant[i]=chunks
                
        
            elif ((arr[i] not in seen) and (maxx not in seen)) and (minn-1<=arr[i]<=maxx-1):
                minn=min(minn,arr[i])
                maxx=max(maxx,arr[i])
                seen.add(arr[i])
                continue
            elif (arr[i] not in seen and (maxx+1==arr[i])) or (maxx==arr[i]):
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
                last=None
                for k in range(till,-1,-1):
                    if arr[k]>comp:
                        last=k
                        chunks=quant[k]
                if last!=None:

                    for j in range(last,till+1):
                        minn=min(minn,arr[j])
                        maxx=max(maxx,arr[j])
                        quant[j]=chunks
            seen.add(arr[i])
                
                
         
        print(quant)
        return chunks
        