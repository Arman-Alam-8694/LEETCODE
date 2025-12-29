class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mapp={}
        for i in allowed:
            temp=i[:2]
            if  temp in mapp:
                mapp[temp].append(i[2])
            else:
                mapp[temp]=[]
                mapp[temp].append(i[2])

        def backtrack(stage,i,j,bottom,nxt):
            if stage==1:
                return True
            # print(bottom)
            temp=bottom[i]+bottom[j]
            if temp in mapp:
                for k in mapp[temp]:
                    nxt.append(k)
                    if stage-1==j:
                        if backtrack(stage-1,0,1,nxt,[]):
                            return True
                        else:
                            nxt.pop()
                        
                    else:
                        if backtrack(stage,i+1,j+1,bottom,nxt):
                            return  True
                        else:
                            nxt.pop()
                        
                        
            else:
                # print(stage,bottom,nxt,i,j)
                return 

        val=backtrack(len(bottom),0,1,bottom,[]) 
        return val if val!=None else False



        