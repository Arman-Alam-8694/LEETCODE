class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def check(listt):
            dictt=defaultdict(int)
            for s,e in listt:
                dictt[s]+=1
                dictt[e-1]-=1
            dictt=sorted(dictt.items(),key=lambda x :x[0])
            run=0
            cnt=-1
            # print(dictt)
            for k,v in dictt:
                run+=v
                if run==0:
                    # print(k,v)
                    cnt+=1
                if cnt==2:
                    return True
            
            return False
        

        x_cords=[]
        y_cords=[]
        for c in rectangles:
            x_cords.append((c[0],c[2]))
            y_cords.append((c[1],c[3]))
          
        # x_cords.sort(key=lambda x:x[0])
        if check(x_cords):
            return True
        # print("y here")
        # y_cords.sort(key=lambda y:y[0])
        if check(y_cords):
            return True
        return False
        
        
        