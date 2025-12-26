class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ty,tn=0,0
        n=len(customers)
        for i in customers:
            if i=="Y":
                ty+=1
            else:
                tn+=1
        penalty=float("inf")
        if ty==n:
            return n
        elif tn==n:
            return 0

        ans=0
        lefty=0
        leftn=0
        for i in range(len(customers)):
            tempy=ty
            tempn=tn
            # if customers[i]=="N":
            #     tempn-=1
            # else:
            #     tempy-=1
            # print("turn ",i)
            # print("best",bestlefty , bestrightn)
            # print("curent",lefty, tempn-leftn)
            ptemp=leftn+(tempy-lefty)
            if ptemp<penalty:
                ans=i
                penalty=ptemp
            if customers[i]=="N":
                leftn+=1
            else:
                lefty+=1
        if customers[-1]=="Y":
            tempy=ty
            tempn=tn
            # if customers[i]=="N":
            #     tempn-=1
            # else:
            #     tempy-=1
            # print("turn ",i)
            # print("best",bestlefty , bestrightn)
            # print("curent",lefty, tempn-leftn)
            if customers[i]=="N":
                leftn+=1
            else:
                lefty+=1
            ptemp=leftn
            if ptemp<penalty:
                ans=n



        return  ans
            

        