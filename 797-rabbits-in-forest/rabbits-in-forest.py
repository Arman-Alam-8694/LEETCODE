class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # 1 1 1
        # 1 - 2
        # 1 1 -2 pairs
        # 1 -2 
        # 1-3 times
        n=len(answers)
        mapp={}
        result=0
        for i in answers:
            if i not in mapp:
                result+=(i+1)
                mapp[i]=1
            else:
                mapp[i]+=1
            if mapp[i]==i+1:
                del mapp[i]
        return result


        