class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        result=0
        queue=deque([])
        seen=set()
        for i in initialBoxes:
            queue.append(i)
            seen.add(i)
        keyy=[0]*1000
        used=[0]*1000
        while queue:
            boxx=queue.popleft()
            if used[boxx]:
                continue

            if status[boxx] or keyy[boxx]:
                result+=candies[boxx]
                used[boxx]=1

                for x in containedBoxes[boxx]:
                    if x not in seen:
                        queue.append(x)
                        seen.add(x)
                    elif keyy[x] and used[y]==0:
                        queue.append(x)

                for y in keys[boxx]:
                    keyy[y]=1
                    if y in seen and used[y]==0:
                        queue.append(y)
        return result