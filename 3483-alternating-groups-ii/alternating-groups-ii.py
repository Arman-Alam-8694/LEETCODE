class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n=len(colors)
        colors+=colors
        result=0
        left=0
        right=0
        while left<n:
            while colors[right+1]!=colors[right] and (right-left+1)<k:
                right+=1
            if (right-left+1)<k:
                right+=1
                left=right
            else:
                result+=1
                left+=1
        return result




