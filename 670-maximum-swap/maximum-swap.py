class Solution:
    def maximumSwap(self, num: int) -> int:
        d_ind={}
        d_count={}
        listt=list(map(int,str(num)))
        n=len(listt)
        for  i in range(n):
            d_ind[listt[i]]=i
            d_count[listt[i]]=d_count.get(listt[i],0)+1
        sortedd=sorted(d_ind.items(),key=lambda x:int(x[0]))
        # print(sortedd)
        # print(d_count)
        max_count=0
        for i in range(n):
            maxx=sortedd[-1][0]
            if listt[i]==maxx:
                max_count+=1
                if max_count==d_count[maxx]:
                    sortedd.pop()
                    max_count=0
            else:
                temp=listt[i]
                listt[i]=listt[sortedd[-1][1]]
                listt[sortedd[-1][1]]=temp
                break

        return int("".join(map(str,listt)))
        