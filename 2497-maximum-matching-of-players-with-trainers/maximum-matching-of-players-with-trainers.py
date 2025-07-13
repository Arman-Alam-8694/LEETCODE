class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        result=0
        t=len(trainers)-1
        for i in range(len(players)-1,-1,-1):
            if t>=0 and trainers[t]>=players[i]:
                result+=1
                t-=1
            elif t<0:
                break
        return result

        