class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([1 for j in grid for i in j if i<0 ])
        