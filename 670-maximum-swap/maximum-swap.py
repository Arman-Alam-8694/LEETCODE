class Solution:
    def maximumSwap(self, num: int) -> int:
        d_ind={}
        listt=list(map(int,str(num)))
        n=len(listt)
        for  i in range(n):
            d_ind[listt[i]]=i
          
        print(d_ind)
        
        for i in range(n):
            for j in range(9,listt[i],-1):
                if (j in d_ind and j!=listt[i]) and i<d_ind[j]:
                    listt[i],listt[d_ind[j]]=listt[d_ind[j]],listt[i]
                    return int("".join(map(str,listt)))
        return int("".join(map(str,listt)))
        