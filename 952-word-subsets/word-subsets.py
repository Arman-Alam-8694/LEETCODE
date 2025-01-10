class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        wtwo=defaultdict(int)
        for w in words2:
            temp=Counter(w)
            for i in temp:
                wtwo[i]=max(wtwo[i],temp[i])
        
        result=[]
        for w in words1:
            temp=Counter(w)
            for i in wtwo:
                if temp[i]<wtwo[i]:
                    break
            else:
                result.append(w)
        return result
