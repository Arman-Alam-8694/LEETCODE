class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights= sorted(heights)
        n=len(heights)
        ans = 0
        for i in range(n):
            if sorted_heights[i]!= heights[i]:
                ans+=1
        return ans