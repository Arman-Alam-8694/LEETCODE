import heapq
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        def search(mono,ch):
            start=0
            end=len(mono)-1
            while start<=end:
                mid=(start+end)//2
                if mono[mid][0]<=ch:
                    end=mid-1
                else:
                    start=mid+1
            return end
            
        q_len=len(queries)
        h_len=len(heights)
        result=[-1]*q_len
        mapp=defaultdict(list)
        
        for idx,hei in enumerate(queries):
            l,r=sorted(hei)
            h=max(heights[l],heights[r])
            if l==r or heights[r]>heights[l]:
                result[idx]=r
            else:
                mapp[r].append((h,idx))
        mono=[]
        for idx in range(h_len-1,-1,-1):
            for q_elem,q_idx in mapp[idx]:
                pos=search(mono,q_elem)
                if pos!=-1:
                    result[q_idx]=mono[pos][1]
                
            while mono and mono[-1][0]<=heights[idx]:
                mono.pop()
            mono.append((heights[idx],idx))
        return result




            
            
      


        