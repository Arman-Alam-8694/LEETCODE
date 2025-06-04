# from collections import deque
# from typing import List

# class Solution:
#     def minMoves(self, classroom: List[str], energy: int) -> int:
#         m, n = len(classroom), len(classroom[0])
#         pos_litter=defaultdict(int)
#         tlit=0
#         x,y=-1,-1
#         for i in range(m):
#             for j in range(n):
#                 if classroom[i][j]=="L":
#                     pos_litter[(i,j)]=tlit
#                     tlit+=1
#                 elif classroom[i][j]=="S":
#                     x=i
#                     y=j

#         print(pos_litter)
#         target=(1<<tlit)-1
#         queue=deque([(x,y,energy,0,0)])
#         directions=[(0,1),(0,-1),(1,0),(-1,0)]
#         seen=[[[-1]*(target+1) for _ in range(n)] for _ in range(m)]
#         # seen[x][y][0]=energy
#         # seen=set()
#         while queue:
#             start,end,cur_energy,cur_litter,steps=queue.popleft()
#             if cur_litter==target:
#                 return steps
#             if classroom[start][end]=="R":
#                 cur_energy=energy
#             if seen[start][end][cur_litter]>=cur_energy:
#                 continue
#             # if cur_energy == 0 and classroom[start][end] != 'R':
#             #     continue
#             seen[start][end][cur_litter]=cur_energy
#             for dx,dy in directions:
#                 nx=dx+start
#                 ny=dy+end
#                 if 0<=nx<m and 0<=ny<n:
                    
#                     if classroom[nx][ny]==".":
#                         queue.append((nx,ny,energy,cur_litter,steps+1))
#                     elif classroom[nx][ny]=="R":
#                         queue.append((nx,ny,cur_energy-1,cur_litter,steps+1))
#                     elif classroom[nx][ny]=="L":
#                         which=pos_litter[(nx,ny)]
#                         tlitter=1<<which|cur_litter
#                         queue.append((nx,ny,cur_energy-1,tlitter,steps+1))
#         return -1


from collections import deque, defaultdict
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        pos_litter = {}
        litter_count = 0
        start_x = start_y = -1
        
        # Map each litter to a unique bit position
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "L":
                    pos_litter[(i, j)] = litter_count
                    litter_count += 1
                elif classroom[i][j] == "S":
                    start_x, start_y = i, j
        
        target_mask = (1 << litter_count) - 1
        queue = deque([(start_x, start_y, energy, 0, 0)])  # x, y, energy, litter_mask, steps
        seen = [[[ -1 for _ in range(1 << litter_count)] for _ in range(n)] for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            x, y, cur_energy, mask, steps = queue.popleft()
            if classroom[x][y]=="R":
                cur_energy=energy
            
            if mask == target_mask:
                return steps

            if seen[x][y][mask] >= cur_energy:
                continue
            seen[x][y][mask] = cur_energy

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != "X":
                    cell = classroom[nx][ny]
                    new_mask = mask
                    if cur_energy==0:
                        # if cell=="R":
                        #      queue.append((nx, ny, energy, new_mask, steps + 1))

                        continue
                    # if next_energy==0:
                    #     if cell=="R":
                    #          queue.append((nx, ny, energy, new_mask, steps + 1))

                    elif cell == "L":
                        idx = pos_litter[(nx, ny)]
                        new_mask |= (1 << idx)
                        queue.append((nx, ny, cur_energy-1, new_mask, steps + 1))
                    elif cell == "R":
                        queue.append((nx, ny, energy, new_mask, steps + 1))  # refill
                    else:  # '.', 'S'
                        queue.append((nx, ny, cur_energy-1, new_mask, steps + 1))
        
        return -1
