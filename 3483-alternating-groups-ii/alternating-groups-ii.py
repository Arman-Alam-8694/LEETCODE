class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n=len(colors)
        result=0
        left=0
        right=0
        while left<n:
            while colors[(right+1)%n]!=colors[(right)%n] and (right-left+1)<k:
                right+=1
            if (right-left+1)<k:
                right+=1
                left=right
            elif (right-left+1)==k:
                result+=1
                left+=1
        return result




