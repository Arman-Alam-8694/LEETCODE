class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        visited = set()
        path = [["."]*n for _ in range(n)]
        result = []
        
        def make_invalid(x, y,visited):
            for i in range(n):
                visited.add((x,i))
                visited.add((i,y))
            dl = dr = y
            row = x
            while row < n:
                row += 1
                dl -= 1
                dr += 1
                if dl >= 0:
                    visited.add((row,dl))
                if dr < n:
                    visited.add((row,dr))
            dl = dr = y
            row = x
            while row > -1:
                row -= 1
                dl -= 1
                dr += 1
                if dl >= 0:
                    visited.add((row,dl))
                if dr < n:
                    visited.add((row,dr))

        # def make_valid(x, y):
        #     for i in range(n):
        #         if (x,i) in visited:
        #             visited.remove((x,i))
        #         if (i,y) in visited:
        #             visited.remove((i,y))
        #     dl = dr = y
        #     row = x
        #     while row < n:
        #         row += 1
        #         dl -= 1
        #         dr += 1
        #         if dl >= 0:
        #             if (row,dl) in visited:
        #                 visited.remove((row,dl))
        #         if dr < n:
        #             if (row,dr) in visited:
        #                 visited.remove((row,dr))
        #     dl = dr = y
        #     row = x
        #     while row > -1:
        #         row -= 1
        #         dl -= 1
        #         dr += 1
        #         if dl >= 0:
        #             if (row,dl) in visited:
        #                 visited.remove((row,dl))
        #         if dr < n:
        #             if (row,dr) in visited:
        #                 visited.remove((row,dr))

        def dfs(row, cnt,visited):
            if cnt == n:
              
                result.append(["".join(row) for row in path])
              
                return
            for i in range(n):
                if (row,i) not in visited:
                    new_visited=visited.copy()
                    path[row][i] = "Q"
                    make_invalid(row,i,new_visited)
                    dfs(row+1, cnt+1,new_visited)
                    path[row][i] = "."
        
        dfs(0,0,visited)
     
        return result