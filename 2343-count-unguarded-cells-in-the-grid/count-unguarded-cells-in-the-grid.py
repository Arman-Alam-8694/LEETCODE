class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        obstacles=set()
        seen=set()
        ans=0
        rem=(m*n)-(len(walls)+len(guards))
        # for i in walls:
        #     wallss.add(tuple(i))
        # for j in guards:
        #     guardss.add(tuple(j))
        for a,b in walls:
            obstacles.add((a,b))
        for a,b in guards:
            obstacles.add((a,b))
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        for x,y in guards:
            for dr,dc in direction:
                r,c=x,y
                while 0<=r+dr<m and 0<=c+dc<n:
                    new=(r+dr,c+dc)
                    if new in obstacles:
                        break
                    elif new not  in seen:
                        rem-=1
                        seen.add(new) 
                    r+=dr
                    c+=dc
                    
                    

            # for x1 in range(x-1,up-1,-1):
            #     if (x1,y) in seen:
            #         continue
            #     elif (x1,y) not in wallss and (x1,y) not in guardss:
            #         rem-=1
            #         seen.add((x1,y))
            #     else:
            #         break
            # for x1 in range(x+1,down+1):
            #     if (x1,y) in seen:
            #         continue
            #     elif (x1,y) not in wallss and (x1,y) not in guardss:
            #         rem-=1
            #         seen.add((x1,y))
            #     else:
            #         break
            # for y1 in range(y+1,right+1):
            #     if (x,y1) in seen:
            #         continue
            #     elif (x,y1) not in wallss and (x,y1) not in guardss:
            #         rem-=1
            #         seen.add((x,y1))
            #     else:
            #         break
            # for y1 in range(y-1,left-1,-1):
            #     if (x,y1) in seen:
            #         continue
            #     elif (x,y1) not in wallss and (x,y1) not in guardss:
            #         rem-=1
            #         seen.add((x,y1))
            #     else:
            #         break

       

        return rem