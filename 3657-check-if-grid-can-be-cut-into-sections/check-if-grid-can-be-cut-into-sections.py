class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def check(listt):
            # dictt=defaultdict(int)
            # for s,e in listt:
            #     dictt[s]+=1
            #     dictt[e-1]-=1
            # dictt=sorted(dictt.items(),key=lambda x :x[0])
            # run=0
            # cnt=-1
            # for k,v in dictt:
            #     run+=v
            #     if run==0:
            #         cnt+=1
            #     if cnt==2:
            #         return True
            listt.sort()
            end=listt[0][1]
            cnt=0
            for i in range(len(listt)):
                if end<=listt[i][0]:
                    cnt+=1
                end=max(end,listt[i][1])
                if cnt==2:
                    return True
            return False
        x_cords=[]
        y_cords=[]
        for c in rectangles:
            x_cords.append((c[0],c[2]))
            y_cords.append((c[1],c[3]))
        if check(x_cords):
            return True
        if check(y_cords):
            return True
        return False
        
        
        