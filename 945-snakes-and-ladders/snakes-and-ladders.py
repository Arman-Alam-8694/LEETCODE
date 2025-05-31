class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        min_steps = [float('inf')]

        def numtocord(num):
            r = (num - 1) // n
            c = (num - 1) % n
            if r % 2 == 1:
                c = n - 1 - c
            return n - 1 - r, c

        result=[float("inf")]
        # @cache
        seen=defaultdict(int)
        def simulate(num,steps):
            if num in seen and steps>=seen[num]:
                return
            seen[num]=steps
            if num==target:
                return 
                
            start=num+1
            end=min(num+6,target)
            for i in range(start,end+1):
                tr,tc=numtocord(i)
                if board[tr][tc]==-1:
                    simulate(i,steps+1)
                else:
                    simulate(board[tr][tc],steps+1)
            return 

        steps=simulate(1,0)
        return seen.get(target,-1)



        