class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        wtwo=defaultdict(int)
        for w in words2:
            temp=Counter(w)
            for i in temp:
                wtwo[i]=max(wtwo[i],temp[i])
        indx=defaultdict(dict)
        for i,w in enumerate(words1):
            temp=Counter(w)
            indx[i]=temp
        result=[]
        for i,k in indx.items():
            for j in wtwo:
                if wtwo[j]>k[j]:
                    break
            else:
                result.append(words1[i])
      
        return result
