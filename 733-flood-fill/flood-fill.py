from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original=image[sr][sc]
        # if original==color:
        #     return image
        Queue=deque([[sr,sc]])
        lower=len(image)-1
        right=len(image[0])-1
        visited=set()
        while Queue:
            nr,nc=Queue.pop()
            visited.add((nr,nc))
            if image[nr][nc]==original :
                image[nr][nc]=color
                if nr-1>=0:
                    if (nr-1,nc) not in visited:
                        Queue.append((nr-1,nc))
                if nr+1<=lower:
                    if (nr+1,nc) not in visited:
                        Queue.append((nr+1,nc))
                if nc+1<=right:
                    if (nr,nc+1) not in visited:
                        Queue.append((nr,nc+1))
                if nc-1>=0:
                    if (nr,nc-1) not in visited:
                        Queue.append((nr,nc-1))
        return image
        