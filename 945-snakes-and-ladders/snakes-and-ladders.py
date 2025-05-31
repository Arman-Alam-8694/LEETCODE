class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        #BACKTRACKING WITH PRUINING O(N^2) AT WORST BUT
        #WITH LOT OF OVERHEAD 

        n = len(board)
        target = n * n

        def numtocord(num):
            r,c=divmod(num-1,n)
            col=c
            row=n-1-r
            if r&1:
                col=n-1-col
            return row,col

        #BACKTRACK WITH PRUNING PART-
        # seen=defaultdict(int)
        # def simulate(num,steps):
        #     if num in seen and steps>=seen[num]:
        #         return
        #     seen[num]=steps
        #     if num==target:
        #         return 
        #     start=num+1
        #     end=min(num+6,target)
        #     for i in range(start,end+1):
        #         tr,tc=numtocord(i)
        #         if board[tr][tc]==-1:
        #             simulate(i,steps+1)
        #         else:
        #             simulate(board[tr][tc],steps+1)
        #     return 

        # simulate(1,0)
        # return seen.get(target,-1)


        #BFS OPTIMISED SOL O(N^2)

        queue=deque([(1,0)])
        seen=set()
        # seen.add(1)
        while queue:
            num,step=queue.popleft()
            if num==target:
                return step
            start=num+1
            end=min(num+6,target)
            for i in range(start,end+1):
            
                tr,tc=numtocord(i)
                if board[tr][tc]==-1 and i not in seen:
                    queue.append((i,step+1))
                    seen.add(i)
                elif board[tr][tc]!=-1 and board[tr][tc] not in seen:
                    queue.append((board[tr][tc],step+1))
                    seen.add(board[tr][tc])
            
        return -1
