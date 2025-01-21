class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        result,prev=maximumHeight[0],maximumHeight[0]
        n=len(maximumHeight)
        
        for i in range(1,n):
            if maximumHeight[i]>=prev:
                prev-=1
                if prev==0:
                    return -1
                result+=prev
            else:
                prev=maximumHeight[i]
                result+=prev
        return result

            
                

