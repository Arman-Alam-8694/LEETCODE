class Solution:
    def coloredCells(self, n: int) -> int:
        sum=1
        for i in range(1,n+1):
            sum+=(i-1)*4
        return sum
