class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # equivalency=defaultdict(str)
        # listt=[]
        # for i,j in zip(s1,s2):
        #     listt.append((i,j))
        # listt.sort()
        # for i,j in listt:
        #     if i>j:
        #         prev=equivalency.get(j,"z")
        #         equivalency[j]=min(prev,j)
        #         equivalency[i]=equivalency[j]
              
        #     else:
        #         prev=equivalency.get(i,"z")
        #         equivalency[i]=min(prev,i)
        #         equivalency[j]=equivalency[i]
      
        # result=[]
        # for i in baseStr:
        #     result.append(equivalency[i])
        # return "".join(result)
        listt=[]
        chartoslot=defaultdict(int)
        cur_slot=0
        chains=defaultdict(set)
        for i,j in zip(s1,s2):
            print(i,j)
            temp1="z"
            temp2="z"
  
            slot1=None
            slot2=None
            if i in chartoslot:
                slot1=chartoslot[i]
                temp1=listt[slot1]
    
            if j in chartoslot:
                slot2=chartoslot[j]
                temp2=listt[slot2]

            if slot1!=None and slot2!=None:
                listt[slot1]=min(temp1,temp2,i,j)
                listt[slot2]=min(temp1,temp2,i,j)
                chartoslot[i]=slot1
                chartoslot[j]=slot2
                chains[slot1].add(slot2)
                chains[slot2].add(slot1)
            elif slot1!=None and slot2==None:
                listt[slot1]=min(temp1,i,j)
                chartoslot[i]=slot1
                chartoslot[j]=slot1 
            elif slot2!=None and slot1==None:
                listt[slot2]=min(temp2,i,j)
                chartoslot[i]=slot2
                chartoslot[j]=slot2
            else:
                listt.append("")
                listt[cur_slot]=min(i,j)
                chartoslot[i]=cur_slot
                chartoslot[j]=cur_slot
                cur_slot+=1

        print(listt)
        print(chains)
        print(chartoslot)
        visited=set()
        for i,k in chains.items():
            if i not in visited:
                for j in k:
                    listt[i]=min(listt[i],listt[j])
                    listt[j]=min(listt[i],listt[j])
            visited.add(i)

        result=[]
        for i in baseStr:
            if i not in chartoslot:
                result.append(i)
            else:
                result.append(listt[chartoslot[i]])
        return "".join(result)
            



        