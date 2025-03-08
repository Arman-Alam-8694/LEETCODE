class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result=float('inf')
        n=len(blocks)
        left=0
        wcnts=0
        for right in range(n):
            if blocks[right]=="W":
                wcnts+=1

            if ((right-left)+1)==k:
                result=min(result,wcnts)
                if blocks[left]=="W":
                    wcnts-=1
                left+=1

        return result
            

        