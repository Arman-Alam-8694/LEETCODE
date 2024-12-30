class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dir=[(0,1),(1,0)]
        def is_valid(x,y):
            if 0<=x<m and 0<=y<n:
                return True
            return False
        @cache
        def recur(i,j):
            if i==m-1 and j==n-1:
                return 1
            ways=0
            for u,v in dir:
                x=i+u
                y=j+v
                if is_valid(x,y):
                    ways+=recur(x,y)
            return ways
        return recur(0,0)
        