class Solution:
    def smallestNumber(self, pattern: str) -> str:
        new_pattern="A"+pattern
        n=len(pattern)
        listt=["-1"]*(n+1)
        print(new_pattern)
        Pidx=0
        lidx=0
        used=set()
        def backtrack(Pidx,lidx,start,used):
          
            if Pidx==n+1:
                return True

            if new_pattern[Pidx]=="A" or new_pattern[Pidx]=="I":
                for i in range(start,10):
                    if i not in used:
                        listt[lidx]=str(i)
                        used.add(i)
                        if backtrack(Pidx+1,lidx+1,i,used):
                            return True
                        used.remove(i)

            else:
                for i in range(start,0,-1):
                    if i not in used:
                        listt[lidx]=str(i)
                        used.add(i)
                        if backtrack(Pidx+1,lidx+1,i,used):
                            return True
                        used.remove(i)
            return False


            




        backtrack(0,0,1,used)
        return "".join(listt)