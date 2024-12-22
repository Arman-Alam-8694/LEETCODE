import heapq
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
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
        min_heap=[]
        for idx,hei in enumerate(heights):
            while min_heap and min_heap[0][0]<hei:
                q_hei,q_idx=heapq.heappop(min_heap)
                result[q_idx]=idx
            for group in mapp[idx]:
                heapq.heappush(min_heap,group)
        return result




        