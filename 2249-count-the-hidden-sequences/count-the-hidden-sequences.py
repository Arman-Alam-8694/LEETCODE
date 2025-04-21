class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        seen=set()
        n=len(differences)
        stack=[]

        def recur(idx,prev,maxx):
            if idx==n:
                # print(maxx)
                return True,maxx
            ahead=differences[idx]+prev
            if lower<=ahead<=upper :
                # print(ahead)
         
                temp=max(maxx,ahead)
                correct,answer=recur(idx+1,ahead,temp)
                if correct:
                    return True,answer

                else:
                    return False,0
            return False,0

        for i in range(lower,upper+1):
            ahead=differences[0]+i
            if lower<=ahead<=upper:
                maxx=max(i,ahead)
                seen.add(ahead)
                seen.add(i)
                correct,ans=recur(1,ahead,maxx)
                if correct:
                    return 1+(upper-ans)
        return 0
                   
                









        