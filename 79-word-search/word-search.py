class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(word)
        row=len(board)
        col=len(board[0])
        def is_valid(x,y,visited):
            if 0<=x<row and 0<=y<col and (x,y) not in visited:
                return True
            return False

        def find(idx,i,j,visited):
            if idx==n:
                return True
            if not is_valid(i,j,visited) or board[i][j]!=word[idx]:
                return False
            visited.add((i,j))
            for u, v in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if find(idx + 1, i + u, j + v, visited):
                    return True
            visited.remove((i,j))
            return False
        
        
      
        for i in range(row):
            for j in range(col):
                if find(0, i, j, set()):
                    return True
            
        return False

        